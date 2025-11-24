---
marp: true
theme: Dictation
header: "資訊科技指南"
footer: "預習與練習"
---

# Lesson 1: What is a computer?

## 1. Computer Definition and Operation Cycle

- **Computer Definition:** A computer is a machine or device **that can receive data and process information, and execute specified tasks**. A computer can also **operate stably, quickly, precisely, and reliably over a long period**.
- **Function:** A computer processes data and outputs information. A computer can store large amounts of data and perform various tasks.
- **Operation Cycle (IPO Cycle):** The correct sequence of computer operation is: **Input → Processing → Output**.
  - **Input:** The computer receives user instructions and data.
  - **Processing:** Data is analyzed, and tasks are executed according to user instructions.
  - **Output:** **Displaying information**. **Displaying the results** is the computer's job during the output stage.

## 2. Types and Comparison of Computers

- **Examples of Computers:**
  - **Common Types:** Smartphone, Laptop computer, Desktop computer, Tablet computer.
  - **Other Applications:** Automated Teller Machine (ATM), POS terminal (Point-of-Sale Terminal), Calculator, Robot, Handheld game console, Smartwatch.
- **Examples of Non-Computer Devices:** USB flash drive, Keyboard, light bulb (because it does not process data).
- **Performance Ranking:** Ranking the efficiency of electronic products from highest to lowest is: **Supercomputer > Desktop Computer > Tablet Computer**. A supercomputer has the highest computing power.
- **Comparison of Type Characteristics:**
  - **Desktop Computer:** Stronger computing power, larger storage capacity, **low portability**.
  - **Laptop Computer:** Built-in display, speakers, camera, webcam, etc. Computing power and storage capacity are usually at an average level, and portability is average. A drawback is the lack of long-term power supply, and the battery may be exhausted.
  - **Tablet Computer:** Better portability. Built-in touch screen, camera, camcorder, etc. Computing power and storage capacity are usually lower.

---

# Lesson 2: Input and Output (I/O) Devices

## 1. Input Devices

- **Function:** To **convert user actions into messages the computer can understand**. These devices allow us to input instructions, or collect data from the outside world and transmit it to the computer.
- **Pointing Devices:** Used for interacting with the computer interface, performing operations such as pointing, clicking, dragging, etc..
  - **Pointing devices include:** Mouse, joystick, trackball, touchpad.
  - **Pointing devices do not include:** Keyboard, touch screen.
  - **Trackball Advantage:** It excels over a mouse in that it requires **less operational space**.
- **Other Input Devices:** Keyboard, motion sensing devices, microphone, scanner, webcam, racing wheel.
- **Devices with both Input and Output capabilities:** Touch screen. A touch screen determines the touch location based on **electrical impulses from the human body**. Another example is a **monitor with built-in speakers**, or **headphones** (if they include a microphone).

## 2. Output Devices

- **Function:** To **convert digital messages into messages understandable by humans**.
- **Common Output Devices:** Monitor, Printer, Speaker, Projector, Headphones/Earphones.
- **OLED Monitor Advantages:** Compared to LCD monitors, they generally have a **higher contrast ratio**, higher consistency of brightness, wider viewing angle, and **lower weight**.

---

## 3. Comparison of Printer Types

| Type of printer     | Consumables      | Printing speed | Quality   | Suitable for              |
| :------------------ | :--------------- | :------------- | :-------- | :------------------------ |
| **Thermal printer** | Thermal paper    | Fast           | Low       | Receipt printing          |
| **Inkjet printer**  | Ink cartridges   | Slow           | Very high | Photo printing            |
| **Laser printer**   | Toner cartridges | Fast           | High      | **Large printing volume** |

- **Thermal Printer Drawbacks:** Requires the use of thermal paper; the printouts **fade over time**.
- **Laser printers** are faster than inkjet printers.
- **3D Printer:** A 3D printer can turn digital 3D models into real objects, used in various fields such as medicine, architecture, art and more.

---

# Lesson 3: System Unit Components

## 1. Components and Functions of the System Unit

- **Components inside the System Unit include:** Motherboard, Central Processing Unit (CPU), Graphics Processing Unit (GPU), Power Supply, Primary Storage (Main memory), Secondary Storage, and Cooling System.
  > Note: The **Keyboard** and **Speaker** **are NOT located on the Motherboard** or inside the System Unit.
- **Motherboard:** It is the computer's **main circuit board**, which serves as **a platform to connect all computer components** (such as the Central Processing Unit, Random Access Memory, and Graphics Processing Unit).
- **Central Processing Unit (CPU):** Often referred to as the **computer's "brain"**. It is responsible for processing data and instructions, and **controls the operation of the computer system**. The CPU is installed on the motherboard.
- **Graphics Processing Unit (GPU):** Similar to the CPU, the GPU is a processor responsible for data processing and command execution. It is primarily responsible for **graphic rendering** and generating images. A GPU generally has more cores, meaning it is more suitable for handling **multitasking** (such as executing AI algorithms).
- **Power Supply:** **Provides power to a computer** for operation, supplying electricity to all components (such as the motherboard, CPU, and storage devices). Since it generates a large amount of heat, a **heat sink** is required.

---

## 2. Primary Storage (Main Memory)

Primary memory (Main memory) is used for **high-speed data access**. It usually refers to RAM and ROM.

| Component Name                 | Volatility (易失性/非易失性) | Data Property (儲存數據屬性)                           | Function/Usage (功能/用途)                                                                   |
| :----------------------------- | :--------------------------- | :----------------------------------------------------- | :------------------------------------------------------------------------------------------- |
| **Random Access Memory (RAM)** | **Volatile**                 | Data **is lost when the computer shuts down**          | **Stores data temporarily** for processing by the CPU                                        |
| **Read-only Memory (ROM)**     | **Non-volatile**             | Data **retains its data when the computer shuts down** | Stores **firmware/a collection of instructions required to boot a computer** (BIOS/Firmware) |

- RAM typically has a larger capacity than Registers.
- The term "Memory" in computer specifications usually refers to **Primary Storage**.

---

# Lesson 4: Central Processing Unit (CPU)

## 1. CPU Components and Their Functions

A CPU is composed of three main components:

- **Arithmetic and Logic Unit (ALU):** Responsible for **arithmetic operations** (e.g., addition, subtraction, multiplication, division) and **logical operations** (e.g., comparison, conjunction/AND, disjunction/OR, inversion/NOT).
- **Control Unit (CU):** Responsible for **decoding instructions**, issuing control signals, controlling the data flow, and commanding the operation of the ALU. The Control Unit is **not responsible for storing data**.
- **Registers:** Located inside the CPU. Used to store the **data values and data addresses currently being processed**. Registers have the **fastest access speed**, but the smallest capacity. CPU registers are at the highest level of the storage hierarchy.

## 2. Factors Affecting CPU Processing Capacity

The processing capacity of the CPU depends on the following factors:

- **Core Count:** A higher number of cores means faster speed for **multitasking**. Multi-core CPUs generally have higher computing power because the workload can be distributed among different cores.
- **Clock Rate:** Refers to the **speed at which a central processor can perform operations**. It is usually measured in gigahertz (GHz). A processor with a higher clock rate usually performs better, but also has **higher energy consumption**.
- **Word Length:** Refers to the length of data a CPU processes at a time (e.g., 32-bit or 64-bit). A **64-bit CPU is NOT necessarily twice as fast as a 32-bit CPU**.

---

## 3. Cooling and Cloud Computing

- **Cooling System:** A CPU generates heat during operation. If overheated, its efficiency will decline or it may even fail. Cooling methods include **Air Cooling (Fan)** and **Liquid Cooling**.
- **Cloud Computing:** A technology that allows people to access **supercomputers** located in the cloud via the Internet. This provides high-performance computing benefits without the need to buy expensive and bulky equipment to keep at home.

---

# Lesson 5: Storage Devices

## 1. Data Units and Number Systems

- **Basic Units:**
  - **Bit (b):** The most fundamental unit of data, representing "0" or "1".
  - **Byte (B):** 1 B = 8 bits.
- **Storage Capacity Ranking (from smallest to largest):** **B < KB < MB < GB < TB**.
  - Conversion relationship: 1 Kilobyte (KB) = $1024$ Bytes (B); 1 Megabyte (MB) = $1024$ KB; 1 Gigabyte (GB) = $1024$ MB; 1 Terabyte (TB) = $1024$ GB.
- **Number System:** Computers use the **Binary number system** (base 2) to process data.

## 2. Secondary Storage

Secondary storage is used to store data for **future use**. All forms of secondary storage are **non-volatile**.

Examples of secondary storage include **Hard disks (HDD)**, **Solid-state drives (SSD)**, and **USB flash drives**.

| Secondary Storage           | Storage Medium     | Data Access Speed                      | Durability                                                     | Cost per Unit Capacity | Other Characteristics                                                                          |
| :-------------------------- | :----------------- | :------------------------------------- | :------------------------------------------------------------- | :--------------------- | :--------------------------------------------------------------------------------------------- |
| **Hard Disk (HDD)**         | **Magnetic media** | **General/Average**                    | Easily damaged by impact.                                      | **Low**                | Has a **large** storage capacity. Contains multiple reading heads and metallic magnetic discs. |
| **Solid-state drive (SSD)** | **Flash memory**   | **Fast** (Faster access time than HDD) | **Durable**. Does not contain moving parts, thus more durable. | **High**               | **Medium** storage capacity. More portable and consumes less power than HDD.                   |

**Other Secondary Storage Devices**:

- **USB Flash Drive:** Composed of **flash memory**. Often used for data backup and transferring data between devices.
- **Optical Disc:** Uses reflective plastic to store data. Examples include Compact Disc (CD) (~700 MB), Digital Versatile Disc (DVD) (~4.7 GB), and Blu-ray Disc (BD) (~25 GB). Optical discs are susceptible to data loss if scratched.
- **Memory Card (e.g., SD Card):** Composed of **flash memory**. Primarily used in mobile devices such as smartphones and digital cameras.

---

## 3. Cloud Storage

- **Providers:** Cloud storage services are offered by Internet Service Providers (ISP). Google Drive is an example of such a service.
- **Advantages:**
  - Users can access data through the Internet **anytime, anywhere** using their devices.
  - Users can easily adjust the storage solution (storage space) to meet their needs.
  - Users **do not need to purchase additional storage equipment**.
  - The risk of data loss is low because service providers automatically back up files.
  - Users can easily share files over the Internet.
- **Disadvantages:**
  - **Reliance on Internet connection**; data cannot be retrieved when offline.
  - Data security depends entirely on the service provider's management.
  - Access time delays may occur if the server is busy, as servers are often shared among multiple users.

## 4. Memory Hierarchy

The Memory Hierarchy categorizes various computer storage devices based on their **data access speed**, **storage capacity**, and **cost per unit capacity**.

**Core Principles**:

- The **higher** the storage device is placed in the hierarchy:
  1.  The **higher** the data access speed.
  2.  The **smaller** the storage capacity.
  3.  The **higher** the cost per unit capacity.

---

### Memory Hierarchy Order (from Fastest/Smallest Capacity to Slowest/Largest Capacity)

Based on the source data, the hierarchy sequence (from top to bottom) is:

1.  **Registers** (Located at the very top of the hierarchy).
2.  **Random Access Memory (RAM)**.
3.  **Solid-state drive (SSD)**.
4.  **Hard Disk**.

---

# Lesson 6: Software

## 1. Distinction Between Software and Hardware

- **Hardware :** Physical devices/components.
- **Software :** **Intangible data and instructions** within a computer system, which help the computer complete tasks.

## 2. System Software**

System software is responsible for **managing computer resources**, controlling hardware operations, and providing a platform for application software.

- Operating System (OS): Manages the operation of computer hardware and programs.
  - **Functions:** Handling process management (scheduling **CPU** execution of programs), **memory management** (allocating **RAM**), peripheral device management, file system management, **hard disk** management, user interface.
  - **Examples:** Microsoft Windows, macOS, iOS, Android, Linux.
- **Utility Programs :** Used to maintain the computer system and improve its efficiency.
  - **Examples:** File management programs, system monitoring software (e.g., Task Manager), virus detection programs (anti-virus scanning), disk defragmentation software, uninstaller programs.
  - **Disk Defragmentation** aims to rearrange files to **improve data access speed and storage efficiency**. However, since **SSDs (Solid-state drives)** have no moving parts, defragmentation is useless and may **reduce its lifespan** due to redundant data writes.
- **Device Drivers :** Classified as **System Software**. Responsible for **controlling the operation of specific hardware**, such as the mouse, keyboard, and speakers.

## 3. Application Software**

Application software helps users perform **specific tasks**.

- **Productivity Software:** Word processors (e.g., Microsoft Word), spreadsheet software (e.g., Microsoft Excel), presentation software (e.g., Microsoft PowerPoint).
- **Communication Software:** Web browsers (e.g., Google Chrome), email clients (e.g., Microsoft Outlook), instant messaging applications (e.g., WhatsApp).
- **Multimedia Software:** Image editing software (e.g., Adobe Photoshop), audio editing software (e.g., Audacity), video editing software (e.g., video rendering, which often relies on the **GPU**).

---

# File Management and Shortcuts

## 1. File Management and File Formats

- **Classification Principles:** Files are generally classified by **File Type**, **Date/Time Sequence**, and **Nature of Activity** . Subfolders should be created to classify files more meticulously .
  - **File Naming:** File names should use **concise text** [Conversation History, 4]. Users should **avoid using special characters** when naming files . Conversely, storing all subject documents in the same folder without classification reduces work efficiency.
- **File Viewing Methods (Windows File Explorer):** Common viewing methods include Large Icons view, Extra Large Icons view, List view, and **Details view** . Choosing the **Details view** should be selected when quickly comparing the file storage time, file size, and file type. "View as Table" is **not a common viewing method** .
- **Common File Formats:** Document files include **PDF**, DOC, DOCX . Image files include GIF, BMP, PNG, JPEG . Video files include AVI .

## 2. Common Keyboard Functions and Shortcuts

- **Function Keys:**
  - **New line/Confirm:** ENTER .
  - **Input symbols (e.g., %):** Press **SHIFT** and the number key simultaneously .
  - **Delete mistyped characters:** BACKSPACE .
  - **Toggle English uppercase/lowercase:** **CAPS LOCK** .
  - **Add space:** SPACE BAR (Spacebar) .
- **Common Shortcuts:**
  - **Copy:** CTRL + **<u>C</u>** .
  - **Paste:** CTRL + **<u>V</u>** .
  - **Cut:** CTRL + **<u>X</u>** .
  - **Undo step/Cancel last action:** If a user wants to undo the previous action (e.g., accidentally deleting an image), they should press the **CTRL + Z** key combination.
  - **Search files/Find:** To quickly find all mentions of a word in a long report, the user can use the **CTRL + F** key combination to activate the **search function**.
  - **Select All:** CTRL + **<u>A</u>** .

---

# Number System Conversion

Humans primarily use the **Decimal system** for calculation. The base of the Decimal system is **$10$**, represented by ten digits ($0, 1, 2, 3, 4, 5, 6, 7, 8, 9$). However, computers use the **Binary system** to represent data. The base of the Binary system is **$2$**, represented by only two digits ($0$ or $1$). The **Bit (b)** is the most fundamental unit of data, being either "0" or "1".

## Binary Conversion to Decimal

**Principle**: To convert a binary number to its decimal equivalent, we multiply each digit of the binary number by its corresponding **place value** (power of $2$), and then sum up the results.

#### Steps and Example: Converting $\mathbf{1101_2}$ to a Decimal number

1.  **Identify the Value and Place Value of each digit**:
    - Starting from the right (the least significant bit), the place values are sequentially $2^0, 2^1, 2^2, 2^3, \dots$.

| Digit             | $1$            | $1$            | $0$            | $1$            |
| :---------------- | :------------- | :------------- | :------------- | :------------- |
| **Place Value**   | $\mathbf{2^3}$ | $\mathbf{2^2}$ | $\mathbf{2^1}$ | $\mathbf{2^0}$ |
| **Decimal Value** | $8$            | $4$            | $2$            | $1$            |

2.  **Calculate the product of each digit and its place value**:

    - $1 \times 2^3 = 1 \times 8 = 8$
    - $1 \times 2^2 = 1 \times 4 = 4$
    - $0 \times 2^1 = 0 \times 2 = 0$
    - $1 \times 2^0 = 1 \times 1 = 1$

3.  **Sum the products to obtain the Decimal number**:
    $$8 + 4 + 0 + 1 = \mathbf{13_{10}}$$
    - Thus, $1101_2 = 13_{10}$.

#### Practice Example

**Example 1**: Convert $1110101_2$ to a Decimal number

- The conversion result for $1110101_2$ is:
  $$\mathbf{1} \times 2^6 + \mathbf{1} \times 2^5 + \mathbf{1} \times 2^4 + \mathbf{0} \times 2^3 + \mathbf{1} \times 2^2 + \mathbf{0} \times 2^1 + \mathbf{1} \times 2^0$$
  $$= 64 + 32 + 16 + 0 + 4 + 0 + 1 = \mathbf{117_{10}}$$

---

## Decimal Conversion to Binary

**Principle**: Use the method of **repeated division by $2$** (short division), record the remainder after each division, and then arrange the last quotient and all remainders in **reverse order** (from last to first).

#### Steps and Example: Converting $\mathbf{105_{10}}$ to a Binary number

1.  **Repeatedly divide by 2**:

    - Divide the decimal number by $2$ and note the remainder. The quotient from the previous step is used as the dividend for the next step. Repeat until the quotient is less than $2$.

    (The process shown in the source is followed):
    $$105 \div 2 = 52 \text{ remainder } \mathbf{1}$$
    $$52 \div 2 = 26 \text{ remainder } \mathbf{0}$$
    $$26 \div 2 = 13 \text{ remainder } \mathbf{0}$$
    $$13 \div 2 = 6 \text{ remainder } \mathbf{1}$$
    $$6 \div 2 = 3 \text{ remainder } \mathbf{0}$$
    $$3 \div 2 = 1 \text{ remainder } \mathbf{1}$$
    $$\mathbf{1} (\text{Final Quotient})$$

2.  **Arrange the Result**:

    - Arrange the final quotient and all the remainders from the last one to the first one.

    - The result arranged in reverse order: $\mathbf{1101001}$

3.  **Obtain the Binary number**:
    - Thus, $105_{10} = \mathbf{1101001_2}$.
