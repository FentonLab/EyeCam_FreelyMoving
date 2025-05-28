import RPi.GPIO as GPIO
import subprocess
import time
import os

TTL_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(TTL_PIN, GPIO.OUT)

# === Prompt user for input ===
output_name = input("Enter output filename (no extension): ").strip()
if not output_name:
    output_name = "recording"
    
# Ensure directory exists
output_dir = "/home/eyecam/eyevideos"
os.makedirs(output_dir, exist_ok=True)

OUTPUT_FILE = os.path.join(output_dir, f"{output_name}.h264")
LOG_FILE = os.path.join(output_dir, f"{output_name}.txt")

while True:
    try:
        RECORD_DURATION = float(input("Enter recording duration (in seconds): "))
        break
    except ValueError:
        print("Please enter a valid number for duration.")

fps = 30
frame_duration = 1 / fps

# === Open the log file ===
with open(LOG_FILE, 'w') as log_file:
    try:
        print(f"Starting camera... Output file: {OUTPUT_FILE}, Duration: {RECORD_DURATION}s")

        # Start the video recording with preview enabled
        process = subprocess.Popen([
            'rpicam-vid',
            '-o', OUTPUT_FILE,
            '-t', str(int(RECORD_DURATION * 1000)),  # convert to ms
            '-p', '0,0,640,480'  # Preview window at position (0,0) with 640x480 size
  	    '--roi', '0.45,0.25,0.5,0.5'              # 2x digital zoom 
        ])

        start_time = time.time()

        while time.time() - start_time < RECORD_DURATION:
            frame_start = time.time()
            timestamp = frame_start - start_time
            log_file.write(f"{timestamp:.3f} sec\n")  # Write the timestamp to the log file
            print(f"Frame at {timestamp:.3f} sec")  # Print timestamp to console

            GPIO.output(TTL_PIN, GPIO.HIGH)
            time.sleep(frame_duration / 2)
            GPIO.output(TTL_PIN, GPIO.LOW)

            time.sleep(max(0, frame_duration / 2 - (time.time() - frame_start)))

        process.wait()
        print("Recording complete")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        GPIO.output(TTL_PIN, GPIO.LOW)
        GPIO.cleanup()
        print("Cleaning up, exiting")