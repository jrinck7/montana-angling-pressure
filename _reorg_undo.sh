#!/usr/bin/env bash
# Undo the 2026-10-13 reorganization. Run: bash _reorg_undo.sh
set -e
cd "$(dirname "$0")"
mv "Figures/angling_pressure_barchart_vertical.png" "Data/angling_pressure_barchart_vertical.png"
mv "Figures/angling_pressure_byriver.png" "Data/angling_pressure_byriver.png"
mv "Figures/angling_pressure_montana_streams_barchart.png" "Data/angling_pressure_montana_streams_barchart.png"
mv "Docs/angler-pressure-survey-summary-2019.pdf" "Data/angler-pressure-survey-summary-2019.pdf"
mv "Docs/angler-pressure-survey-summary-2020.pdf" "Data/angler-pressure-survey-summary-2020.pdf"
mv "Notebook/build/Project1.aux" "Notebook/Project1.aux"
mv "Notebook/build/Project1.log" "Notebook/Project1.log"
mv "Notebook/build/Project1.out" "Notebook/Project1.out"
mv "Notebook/build/Project1_JansenRinck.aux" "Notebook/Project1_JansenRinck.aux"
mv "Notebook/build/Project1_JansenRinck.log" "Notebook/Project1_JansenRinck.log"
mv "Notebook/build/Project1_JansenRinck.out" "Notebook/Project1_JansenRinck.out"
mv "Reports/drafts/Project1_Prototype.pdf" "Reports/Project1_Prototype.pdf"
mv "Reports/drafts/Project1_Prototype3.pdf" "Reports/Project1_Prototype3.pdf"
mv "Reports/drafts/Project1_prototype_2.pdf" "Reports/Project1_prototype_2.pdf"
mv "Reports/drafts/Project1_Launch_JR_9.3.26..pdf" "Reports/Project1_Launch_JR_9.3.26..pdf"
