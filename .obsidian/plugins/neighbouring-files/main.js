/*
THIS IS A GENERATED/BUNDLED FILE BY ESBUILD
if you want to view the source, please visit the github repository of this plugin
*/

var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

// src/main.ts
var main_exports = {};
__export(main_exports, {
  default: () => NeighbouringFileNavigatorPlugin
});
module.exports = __toCommonJS(main_exports);

// src/NeighbouringFileNavigator.ts
var import_obsidian = require("obsidian");
var NeighbouringFileNavigator = class {
  static getNeighbouringFiles(file) {
    var _a;
    const files = (_a = file == null ? void 0 : file.parent) == null ? void 0 : _a.children;
    const filteredFiles = files == null ? void 0 : files.filter((f) => f instanceof import_obsidian.TFile && f.extension === "md");
    const sortedFiles = filteredFiles == null ? void 0 : filteredFiles.sort((a, b) => a.basename.localeCompare(b.basename, void 0, {
      numeric: true,
      sensitivity: "base"
    }));
    return sortedFiles;
  }
};

// src/main.ts
var import_obsidian2 = require("obsidian");
var NeighbouringFileNavigatorPlugin = class extends import_obsidian2.Plugin {
  navigateToNeighbouringFile(next) {
    const activeFile = this.app.workspace.getActiveFile();
    if (!activeFile)
      return;
    const files = NeighbouringFileNavigator.getNeighbouringFiles(activeFile);
    if (!files)
      return;
    const currentItem = files.findIndex(
      (item) => item.name === activeFile.name
    );
    const toFile = next ? files[(currentItem + 1) % files.length] : files[currentItem == 0 ? files.length - 1 : (currentItem - 1) % files.length];
    this.app.workspace.getLeaf(false).openFile(toFile);
  }
  async onload() {
    this.addCommand({
      id: "next",
      name: "Navigate to next file",
      callback: () => this.navigateToNeighbouringFile(true)
    });
    this.addCommand({
      id: "prev",
      name: "Navigate to previous file",
      callback: () => this.navigateToNeighbouringFile(false)
    });
  }
  onunload() {
  }
};

/* nosourcemap */