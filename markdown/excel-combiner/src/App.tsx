import React, { useState } from 'react';
import * as XLSX from 'xlsx';
import { Upload, Download, FileSpreadsheet, AlertCircle, CheckCircle, Layers } from 'lucide-react';

interface FileInfo {
  name: string;
  sheetName?: string;
  rows: number;
  columns: number;
}

interface ResultData {
  workbook: XLSX.WorkBook;
  fileInfo: FileInfo[];
  totalSheets?: number;
  totalRows?: number;
  totalColumns?: number;
  mode: string;
}

export default function ExcelCombiner() {
  const [files, setFiles] = useState<File[]>([]);
  const [processing, setProcessing] = useState(false);
  const [result, setResult] = useState<ResultData | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [combineMode, setCombineMode] = useState<'separate' | 'single'>('separate');

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFiles = Array.from(e.target.files || []);
    setFiles(selectedFiles);
    setResult(null);
    setError(null);
  };

  const combineExcelFiles = async () => {
    if (files.length === 0) {
      setError('Please select at least one Excel file');
      return;
    }

    setProcessing(true);
    setError(null);

    try {
      if (combineMode === 'separate') {
        await combineSeparateSheets();
      } else {
        await combineSingleSheet();
      }
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Unknown error occurred';
      setError(`Error combining files: ${errorMessage}`);
    } finally {
      setProcessing(false);
    }
  };

  const combineSeparateSheets = async () => {
    const workbook = XLSX.utils.book_new();
    const fileInfo: FileInfo[] = [];

    for (const file of files) {
      const data = await readExcelFile(file);
      if (data && data.length > 0) {
        let sheetName = file.name.replace(/\.(xlsx|xls)$/i, '').slice(0, 31);
        
        let counter = 1;
        let finalSheetName = sheetName;
        while (workbook.SheetNames.includes(finalSheetName)) {
          finalSheetName = `${sheetName.slice(0, 28)}_${counter}`;
          counter++;
        }

        const ws = XLSX.utils.json_to_sheet(data);
        XLSX.utils.book_append_sheet(workbook, ws, finalSheetName);
        
        fileInfo.push({
          name: file.name,
          sheetName: finalSheetName,
          rows: data.length,
          columns: Object.keys(data[0] || {}).length
        });
      }
    }

    if (workbook.SheetNames.length === 0) {
      setError('No data found in the selected files');
      return;
    }

    setResult({
      workbook: workbook,
      fileInfo: fileInfo,
      totalSheets: workbook.SheetNames.length,
      mode: 'separate'
    });
  };

  const combineSingleSheet = async () => {
    const allData: any[] = [];
    const fileInfo: FileInfo[] = [];

    for (const file of files) {
      const data = await readExcelFile(file);
      if (data && data.length > 0) {
        const dataWithSource = data.map((row: any) => ({
          ...row,
          '_source_file': file.name
        }));
        allData.push(...dataWithSource);
        fileInfo.push({
          name: file.name,
          rows: data.length,
          columns: Object.keys(data[0] || {}).length
        });
      }
    }

    if (allData.length === 0) {
      setError('No data found in the selected files');
      return;
    }

    const allColumns = new Set<string>();
    allData.forEach((row: any) => {
      Object.keys(row).forEach(col => allColumns.add(col));
    });

    const normalizedData = allData.map((row: any) => {
      const normalizedRow: any = {};
      allColumns.forEach(col => {
        normalizedRow[col] = row[col] !== undefined ? row[col] : '';
      });
      return normalizedRow;
    });

    const workbook = XLSX.utils.book_new();
    const ws = XLSX.utils.json_to_sheet(normalizedData);
    XLSX.utils.book_append_sheet(workbook, ws, 'Combined Data');

    setResult({
      workbook: workbook,
      fileInfo: fileInfo,
      totalRows: normalizedData.length,
      totalColumns: allColumns.size,
      mode: 'single'
    });
  };

  const readExcelFile = (file: File): Promise<any[]> => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      
      reader.onload = (e) => {
        try {
          if (!e.target?.result) {
            reject(new Error('Failed to read file'));
            return;
          }
          const data = new Uint8Array(e.target.result as ArrayBuffer);
          const workbook = XLSX.read(data, { type: 'array' });
          const firstSheet = workbook.Sheets[workbook.SheetNames[0]];
          const jsonData = XLSX.utils.sheet_to_json(firstSheet);
          resolve(jsonData);
        } catch (err) {
          reject(err);
        }
      };
      
      reader.onerror = () => reject(new Error(`Failed to read ${file.name}`));
      reader.readAsArrayBuffer(file);
    });
  };

  const downloadCombined = () => {
    if (!result) return;
    
    const timestamp = new Date().toISOString().slice(0, 10);
    const filename = `combined_excel_${timestamp}.xlsx`;
    
    XLSX.writeFile(result.workbook, filename);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-8">
      <div className="max-w-4xl mx-auto">
        <div className="bg-white rounded-lg shadow-lg p-8">
          <div className="flex items-center gap-3 mb-6">
            <FileSpreadsheet className="w-8 h-8 text-indigo-600" />
            <h1 className="text-3xl font-bold text-gray-800">Excel File Combiner</h1>
          </div>
          
          <p className="text-gray-600 mb-6">
            Combine multiple Excel files into one workbook with different options.
          </p>

          {/* Combine Mode Selection */}
          <div className="mb-6 p-4 bg-gray-50 rounded-lg">
            <h3 className="font-semibold text-gray-700 mb-3">Combine Mode:</h3>
            <div className="space-y-3">
              <label className="flex items-start gap-3 cursor-pointer">
                <input
                  type="radio"
                  name="mode"
                  value="separate"
                  checked={combineMode === 'separate'}
                  onChange={(e) => setCombineMode(e.target.value as 'separate' | 'single')}
                  className="mt-1"
                />
                <div>
                  <div className="font-medium text-gray-800 flex items-center gap-2">
                    <Layers className="w-4 h-4" />
                    Separate Worksheets (Recommended)
                  </div>
                  <p className="text-sm text-gray-600">Each file becomes a separate worksheet in one Excel file</p>
                </div>
              </label>
              
              <label className="flex items-start gap-3 cursor-pointer">
                <input
                  type="radio"
                  name="mode"
                  value="single"
                  checked={combineMode === 'single'}
                  onChange={(e) => setCombineMode(e.target.value as 'separate' | 'single')}
                  className="mt-1"
                />
                <div>
                  <div className="font-medium text-gray-800">Single Worksheet</div>
                  <p className="text-sm text-gray-600">All data merged into one worksheet with all columns</p>
                </div>
              </label>
            </div>
          </div>

          {/* File Upload */}
          <div className="mb-6">
            <label className="flex flex-col items-center justify-center w-full h-32 border-2 border-dashed border-indigo-300 rounded-lg cursor-pointer hover:bg-indigo-50 transition-colors">
              <div className="flex flex-col items-center justify-center pt-5 pb-6">
                <Upload className="w-10 h-10 text-indigo-400 mb-2" />
                <p className="text-sm text-gray-600">
                  <span className="font-semibold">Click to upload</span> Excel files
                </p>
                <p className="text-xs text-gray-500 mt-1">XLSX, XLS formats supported</p>
              </div>
              <input
                type="file"
                className="hidden"
                accept=".xlsx,.xls"
                multiple
                onChange={handleFileSelect}
              />
            </label>
          </div>

          {/* Selected Files */}
          {files.length > 0 && (
            <div className="mb-6">
              <h3 className="font-semibold text-gray-700 mb-2">Selected Files ({files.length}):</h3>
              <div className="space-y-1">
                {files.map((file, idx) => (
                  <div key={idx} className="text-sm text-gray-600 bg-gray-50 px-3 py-2 rounded">
                    {file.name} ({(file.size / 1024).toFixed(1)} KB)
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Combine Button */}
          <button
            onClick={combineExcelFiles}
            disabled={files.length === 0 || processing}
            className="w-full bg-indigo-600 text-white py-3 rounded-lg font-semibold hover:bg-indigo-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors mb-6"
          >
            {processing ? 'Processing...' : 'Combine Files'}
          </button>

          {/* Error Message */}
          {error && (
            <div className="mb-6 p-4 bg-red-50 border border-red-200 rounded-lg flex items-start gap-3">
              <AlertCircle className="w-5 h-5 text-red-600 mt-0.5 flex-shrink-0" />
              <p className="text-red-800 text-sm">{error}</p>
            </div>
          )}

          {/* Success Result */}
          {result && (
            <div className="space-y-4">
              <div className="p-4 bg-green-50 border border-green-200 rounded-lg flex items-start gap-3">
                <CheckCircle className="w-5 h-5 text-green-600 mt-0.5 flex-shrink-0" />
                <div className="flex-1">
                  <p className="text-green-800 font-semibold mb-2">Files combined successfully!</p>
                  {result.mode === 'separate' ? (
                    <p className="text-sm text-green-700">
                      Total worksheets: {result.totalSheets}
                    </p>
                  ) : (
                    <p className="text-sm text-green-700">
                      Total rows: {result.totalRows} | Total columns: {result.totalColumns}
                    </p>
                  )}
                </div>
              </div>

              {/* File Info */}
              <div className="bg-gray-50 rounded-lg p-4">
                <h3 className="font-semibold text-gray-700 mb-3">
                  {result.mode === 'separate' ? 'Worksheets Created:' : 'Source Files Summary:'}
                </h3>
                <div className="space-y-2">
                  {result.fileInfo.map((info, idx) => (
                    <div key={idx} className="text-sm text-gray-600">
                      <div className="flex justify-between">
                        <span className="font-medium">{info.name}</span>
                        <span className="text-gray-500">{info.rows} rows, {info.columns} columns</span>
                      </div>
                      {info.sheetName && (
                        <div className="text-xs text-indigo-600 mt-1">→ Worksheet: "{info.sheetName}"</div>
                      )}
                    </div>
                  ))}
                </div>
              </div>

              {/* Download Button */}
              <button
                onClick={downloadCombined}
                className="w-full bg-green-600 text-white py-3 rounded-lg font-semibold hover:bg-green-700 transition-colors flex items-center justify-center gap-2"
              >
                <Download className="w-5 h-5" />
                Download Combined Excel
              </button>
            </div>
          )}
        </div>

        {/* Instructions */}
        <div className="mt-6 bg-white rounded-lg shadow p-6">
          <h3 className="font-semibold text-gray-800 mb-3">How it works:</h3>
          <div className="space-y-4">
            <div>
              <h4 className="text-sm font-semibold text-indigo-600 mb-2">Separate Worksheets Mode:</h4>
              <ul className="space-y-1 text-sm text-gray-600 ml-4">
                <li>• Each Excel file becomes a separate worksheet</li>
                <li>• Original column structure is preserved</li>
                <li>• Sheet names are based on file names</li>
              </ul>
            </div>
            <div>
              <h4 className="text-sm font-semibold text-indigo-600 mb-2">Single Worksheet Mode:</h4>
              <ul className="space-y-1 text-sm text-gray-600 ml-4">
                <li>• All data merged into one worksheet</li>
                <li>• All columns from all files are included</li>
                <li>• A "_source_file" column tracks the origin</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}