<p align="center">
  <img width="250" height="250" src="newlogor.ico">
</p>

<h1 align="center">autosort</h1>
<h4 align="center">A lightweight file-copying interface.</h4>

<div align="center">
  <a><a href="https://github.com/vihdutta/autosort"><img src="https://img.shields.io/github/license/vihdutta/autosort?color=yellow&amp;logo=MIT" alt="GitHub license"></a>
  <img src="https://img.shields.io/codeclimate/tech-debt/vihdutta/autosort?color=yellow" alt="Code Climate technical debt">
  <img src="https://img.shields.io/github/v/release/vihdutta/autosort?color=yellow&amp;include_prereleases" alt="GitHub release (latest by date including pre-releases)">
  <img src="https://img.shields.io/lgtm/grade/python/github/vihdutta/autosort?color=yellow" alt="LGTM Grade">
</div>

## Preview

<div align="center">
  <img src="media/demos/demo.gif" alt="demo.gif" />
</div>

## What is autosort?
Autosort is a lightweight file-copying interface. It allows you to copy several directories to another folder while also having the ability to create folders for each file type, create folders for each source directory, and more! One of its distinct features is making sure files are copied without overwriting each other by adding a (1), (2), (3), etc. If you want to have these features and more, download the single executable here: https://github.com/vihdutta/autosort/releases/latest

## Features

### Low resource usage

Autosort uses an average of **15mb** of RAM on startup. Even after heavy load, autosort averages below **30mb** of memory usage. Under heavy load, CPU usage is at an average of **10%**.

##### Resource usage benchmarks as of v1.0

<div align="center">
  <img src="media/benchmarks/startup_autosort.png">
  <h6>After startup.</h6>
  <img src="media/benchmarks/copying_autosort.png">
  <h6>While copying 2,000x, 64kb files.</h6>
  <img src="media/benchmarks/12000_autosort.png">
  <h6>After copying 2,000x, 64kb files 5x times (12,000 files total).</h6>
</div>

###### ***Performance depends mainly on system specifications. This benchmark was tested on a computer with these relevant specifications: Intel i7-4770, 16gb DDR3 RAM (1600mhz), Samsung SSD 860 EVO 1TB.**

### Versatility

Autosort has all dependencies bundled up into a single executable. This allows autosort to be a "plug-in-and-play" program and be used from even a flash drive.

### Realtime Progress Display

Autosort is configured with a terminal-like progress displayer eliminating the usage of inaccurate progress bars. The progress displayer presents exactly what operation the program is processing with almost no cost in performance.

## Usage

Select the source directory (files you want to copy) and the destination directory (where you want to copy to) which appears on a button press. Note: the source directory selects all files inside that directory. Click the run button to start the copying process.

## Installation

Download the latest version of autosort from https://github.com/vihdutta/autosort/releases/latest. Since autosort is an executable file (.exe), your anti-virus may prevent you from running autosort. You may have to exclude autosort from your anti-virus software prior to usage.

## Some Future Considerations
These all may or may not be implemented. Each box below may recieve a checkmark when they are being worked on, or have been acknowledged.

- [x] Beautify README.md
- [x] Organize repository files
- [ ] Decrease startup time
- [ ] Reduce CPU usage while "Enumerating..."
- [ ] Reduce time usage while "Enumerating..."
- [x] Create a higher resolution demo gif
- [x] Increase readability and quality of code
- [ ] Reduce CPU usage while moving GUI
- [ ] Stop the user from pressing the run button while a process is already running
- [ ] Research Hashlib
- [ ] Research Pathlib
- [x] Use underscores with variable names.
- [ ] Use tests.
- [ ] Split copyfromdirs()
- [ ] Make fcmethods more explicit.
