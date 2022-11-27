import librosa
import scipy.stats
import numpy as np
import tkinter
import tkinter.filedialog
import librosa.display
import matplotlib.pyplot as plt
import math

def prediction(median):
    if median > 0.001:
        return "Speech"
    else:
        return "Music"

def strip(input):
    output = ""
    for i in input:
        if i == "/":
            output = ""
        else:
            output += i
    return output

choice = 'y'

print("*************")
print("* Sound-aid *")
print("*************")
print()


while choice != 'n':

    print("> Select file")
    print()

    try:
        # 1. Get the file path to an included audio example
        # filename = librosa.example('nutcracker')
        # filename = "input/Sweet D'Buster - Bread (Gigs).mp3"
        #filename = "input/New Voice-over Aug 2022.mp3"

        file = tkinter.filedialog.askopenfile(mode='r')
        #print("General attributes")
        #print("==================")
        print("File name: ", strip(file.name))
        #print(f"File-name: {file.name}")
        #print(f"Encoding:  {file.encoding}")
        print()

        filename = file.name

        # 2. Load the audio as a waveform `y`
        #    Store the sampling rate as `sr`
        y, sr = librosa.load(filename)

        # 3. Run the default beat tracker
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

        #print("Audio attributes")
        #print("==================")
        print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
        #print()

        # 4. Convert the frame indices of beat events into timestamps
        beat_times = librosa.frames_to_time(beat_frames, sr=sr)
        #print(f"Beat times: {beat_times}")
        onset_env = librosa.onset.onset_strength(y=y, sr=sr)
        #print(f"Onset_env: {onset_env}")
        pulse = librosa.beat.plp(onset_envelope=onset_env, sr=sr)
        #print(f"Pulse: {pulse}")
        #print()
        print(f"Median: {np.median(pulse)}")
        print(f"Mean: {np.mean(pulse)}")
        print(f"Standard deviation: {np.std(pulse)}")
        print(f"Variance: {np.var(pulse)}")
        print(f"Skewness: {scipy.stats.skew(pulse)}")
        print(f"Kurtosis: {scipy.stats.kurtosis(pulse)}")
        print()
        print(f"Tempo / Skew: {round(np.mean(pulse) / scipy.stats.skew(pulse),3)}")
        print(f"Tempo / Kurtosis: {round(np.mean(pulse) / scipy.stats.kurtosis(pulse),3)}")
        print(f"Tempo / Variance: {round(np.mean(pulse) / np.var(pulse),3)}")
        print(f"Tempo / Std: {round(np.mean(pulse) / np.std(pulse),3)}")
        print()
        

        # ---------------------------------------------------------------
        prior = scipy.stats.lognorm(loc=np.log(120), scale=120, s=1)
        # ---------------------------------------------------------------




        pulse_lognorm = librosa.beat.plp(onset_envelope=onset_env, sr=sr,
                                        prior=prior)
        beat_track = librosa.beat.beat_track( y=y, sr=sr)
        #print(f"Beat_track: {beat_track}")
        #print(f"tempo: {tempo}")
        #print(f"beat_frames: {beat_frames}")
        #print()
        #print(f"Pulse lognorm: {pulse_lognorm}")
        #print(F"Pulse lognorm (min): {np.min(pulse_lognorm)}")
        #print(F"Pulse lognorm (max): {np.max(pulse_lognorm)}")
        #print(F"Pulse lognorm (mean): {np.mean(pulse_lognorm)}")
        #print(F"Pulse lognorm (median): {np.median(pulse_lognorm)}")
        #print(F"Pulse lognorm (std): {np.std(pulse_lognorm)}")
        #print(F"Pulse lognorm (var): {np.var(pulse_lognorm)}")
        #print(F"Pulse lognorm (sum): {np.sum(pulse_lognorm)}")
        #print(F"Pulse lognorm (size): {np.size(pulse_lognorm)}")
        #sum_div_size = np.sum(pulse_lognorm) / np.size(pulse_lognorm)
        #print(F"Sum / Size: {sum_div_size}")
        #print(F"Pulse lognorm (shape): {np.shape(pulse_lognorm)}")
        #print(F"Pulse lognorm (ndim): {np.ndim(pulse_lognorm)}")
        #print(F"Pulse lognorm (nbytes): {pulse_lognorm.nbytes}")
        #print(F"Pulse lognorm (itemsize): {pulse_lognorm.itemsize}")
        #print(F"Pulse lognorm (data): {pulse_lognorm.data}")
        #print(F"Pulse lognorm (dtype): {pulse_lognorm.dtype}")
        #print(F"Pulse lognorm (flags): {pulse_lognorm.flags}")
        #print(F"Pulse lognorm (flat): {pulse_lognorm.flat}")
        #print(F"Pulse lognorm (strides): {pulse_lognorm.strides}")
        #pl_T_mean = np.mean(pulse_lognorm.T)
        #print(F"Pulse lognorm (T) mean: {pl_T_mean}")
        #pl_T_std = np.std(pulse_lognorm.T)
        #print(F"Pulse lognorm (T) spread: {pl_T_std}")
        #print(F"Pulse lognorm (base): {pulse_lognorm.base}")
        #pl_real_mean = np.mean(pulse_lognorm.real)
        #print(F"Pulse lognorm (real): {pl_real_mean}")
        #pl_real_std = np.std(pulse_lognorm.real)
        #print(F"Pulse lognorm (spread) {pl_real_std}")
        #print(F"Pulse lognorm (imag): {pulse_lognorm.imag}")
        #print(F"Pulse lognorm (ctypes): {pulse_lognorm.ctypes}")


        print()

       

       
        
        """
        for i in range(0, len(pulse_lognorm)):
            tmp_str = int(pulse_lognorm[i] * 50) * '▮'
            print(f"{i}: {tmp_str}")




        print("Audio visualisation")
        print("==================")
        print()
        librosa.display.waveshow(y, sr=sr)        
        librosa.display.specshow(melspec, sr=sr, x_axis='time', y_axis='mel')
        librosa.display.specshow(librosa.power_to_db(melspec, ref=np.max), y_axis='mel', fmax=8000, x_axis='time')
        #plt.show()
        


        print()
        print(50 * "*" )
        print(f"Prediction: This file is of the following type: {prediction(np.median(pulse_lognorm))}")
        print(50 * "*" )
        print()
        """
    except ValueError as e:
        print(f"*** Error: {e} ***")

    print()
    choice = input("Another file? (Y/n) ")

