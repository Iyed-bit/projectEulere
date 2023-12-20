import time
import winsound  # Windows-specific module for sound

def chronometer(duration_minutes):
    input("Press Enter to start the chronometer.")
    
    # Convert duration from minutes to seconds
    duration_seconds = duration_minutes * 60
    
    start_time = time.time()

    try:
        while True:
            elapsed_time = time.time() - start_time
            formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
            print(f"\rElapsed Time: {formatted_time}", end="", flush=True)

            if elapsed_time >= duration_seconds:
                break

            time.sleep(1)
    except KeyboardInterrupt:
        pass

    end_time = time.time()
    total_time = end_time - start_time
    formatted_total_time = time.strftime("%H:%M:%S", time.gmtime(total_time))
    print(f"\nTotal Elapsed Time: {formatted_total_time}")

    # Beep when the duration is over
    winsound.Beep(1000, 1000)  # Frequency: 1000 Hz, Duration: 1000 ms

if __name__ == "__main__":
    duration_minutes = int(input("Enter the duration in minutes: "))
    chronometer(duration_minutes)
