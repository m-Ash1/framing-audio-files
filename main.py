from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

# Load a WAV file
sampleRate, audioData = wavfile.read('aaaa.wav')

# Create a time array
time = np.arange(0, len(audioData)) / sampleRate

# Plot the audio signal
plt.plot(time, audioData)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()

# Print the sample rate and shape of the audio data
print(f'Sample rate: {sampleRate}')
print(f'Audio data shape: {len(audioData)}')

arr = []
matrix = []
overLap = []


def framing(audioData, sampleRate, frameSize, overlapSize, wt):
    global overLap
    global arr
    frameSamples = int((frameSize / 1000) * sampleRate)
    overlapSamples = int((overlapSize / 1000) * sampleRate)

    index = 0
    for i in audioData:
        if index < frameSamples - len(overLap):
            index += 1
            arr.append(i)
        else:
            # truncate
            overLap = arr[frameSamples - overlapSamples:].copy()
            matrix.append(arr.copy())
            arr.clear()

            arr = overLap.copy()
            arr.append(i)
            index = 1
    matrix.append(arr.copy())


framing(audioData, sampleRate, 20, 10, None)

# converting matrix into 1d array
matrix1d = []
for row in matrix:
    matrix1d.extend(row)

time = np.arange(0, len(matrix1d)) / sampleRate

plt.plot(time, matrix1d)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()
