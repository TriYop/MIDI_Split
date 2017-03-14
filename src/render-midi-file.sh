#!/usr/bin/env bash
#
PYTHON=/usr/bin/python3

TIMIDITY_CONFIG=/opt/etc/timidity-render.cfg
TIMIDITY_AMPLIFICATION=70     # 70 is default value
TIMIDITY_VOLUME_CURVE=1.661   # Ideal curve
TIMIDITY_CACHE_SIZE=67108864  # 64MB
TIMIDITY_SAMPLING_RATE=48000  # 48kHz


#-- TIMIDITY CONSTANTS

# TIMIDITY MODULES
TIMIDITY_MODULE_DEFAULT=0
TIMIDITY_MODULE_ROLAND_SC55=1
TIMIDITY_MODULE_ROLAND_SC88=2
TIMIDITY_MODULE_ROLAND_SC88PRO=3
TIMIDITY_MODULE_ROLAND_SC8850=4
TIMIDITY_MODULE_YAMAHA_MU50=16
TIMIDITY_MODULE_YAMAHA_MU80=17
TIMIDITY_MODULE_YAMAHA_MU90=18
TIMIDITY_MODULE_YAMAHA_MU100=19
TIMIDITY_MODULE_SBLIVE=32
TIMIDITY_MODULE_SBAUDIGY=33
TIMIDITY_MODULE_SPECIAL1=112
TIMIDITY_MODULE_DEBUG=127



#====================================================================================================================
SCRIPT_DIR=$( readlink -f $0 | xargs -i dirname {} )

INPUT_FILE="$1"
OUTPUT_DIR="$2"

# TODO: check parameters value before using them
if [ ! -f ${INPUT_FILE} ]; then
  echo "Missing file: ${INPUT_FILE}"
  exit 1
fi
if [ ! -d ${OUTPUT_DIR} ]; then
  mkdir -p ${OUTPUT_DIR}
fi


${PYTHON} ${SCRIPT_DIR}/miditools/MIDI_split.py --input ${INPUT_FILE} --output ${OUTPUT_DIR}

for MIDIFILE in $(find ${OUTPUT_DIR} -name '*.mid'); do
    WAVEFILE=$(echo ${MIDIFILE} | sed -r -e 's/.mid$/.wav/i')

    timidity -invt\
          -c ${TIMIDITY_CONFIG}\
          --volume-curve ${TIMIDITY_VOLUME_CURVE}\
          --anti-alias\
          --module=${TIMIDITY_MODULE_SBLIVE}\
          -A${TIMIDITY_AMPLIFICATION}\
          --control-ratio=1\
          -Ow\
          --output-mono\
          --output-24bit\
          --resample=n\
          --interpolation=5\
          --sampling-freq=${TIMIDITY_SAMPLING_RATE}\
          --no-polyphony-reduction\
          --audio-buffer=10/100\
          --cache-size=${TIMIDITY_CACHE_SIZE}\
          --no-realtime-load\
          --voice-queue=0\
          ${MIDIFILE} -o ${WAVEFILE}.wav

done