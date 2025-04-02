"""
ENGG1001 Assignment 1
Semester 1, 2024
"""
from a1_support import * 


# Fill these in with your details
__author__ = "Zac Carpenter"
__email__ = "z.carpenter@uqconnect.edu.au"
__date__ = "22/03/2024"


# Write your functions here
from scipy.io.wavfile import read, write
import numpy as np
import matplotlib.pyplot as plt

def read_wav_file(input_filename):
    """
    Takes a .wav filename as an input parameter and returns the sampling rate
    (i.e. the number of signal samples per second) and a tuple containing all
    the audio  samples. The function only reads mono (i.e. single channel
    .wav files).

    Parameters:
        input_filename (str): The name of the input .wav file

    Returns:
        tuple(int, tuple(int)): The first integer of the tuple represents the
        sampling rate, the second element of the tuple is another tuple
        containing the samples of the input audio.
    """
    sr_value, x_value = read(input_filename)
    x_value = tuple((int(i) for i in x_value))
    return sr_value, x_value

def write_wav_file(output_file_name, sr_value, audio):
    """
    Outputs a mono (single channel) signal to a .wav file

    Parameters:
        output_filename (str): The name of the output .wav file
        sr_value (int): The sampling rate
        audio (tuple): A tuple of samples of the output signal

    Returns:
        None.
    """
    audio = np.array(audio).astype(np.int16)
    write(output_file_name, sr_value, audio)
    
def determine_time_duration(sample_rate, number_samples):
    """
    Determines the time duration of an audio sample given its sample rate and the number of samples in the audio file
    by dividing the number of samples - 1 by the sample rate.

    Parameters:
        sample_rate(int): The rate at which the audio samples are played.
        number_smaples(int): The number of audio samples in the file.
    Returns:
        int: The time duration of the sample. 
        
    """
    return (number_samples - 1) / sample_rate
   

def concatenate_audios(audio_1, audio_2):
    """
    Takes two audio tuples and concatenates them into a single tuple.
    
    Parameters:
        audio_1(tuple(float)): The first input audio as prompted by the user.
        audio_2(tuple(float)): The second input audio as prompted by the user.
    Returns:
        audio_1 + audio_2(tuple(int)): concatenated result of audio_1 and audio_2.
    """
    return audio_1 + audio_2


def scale_audio(audio_in, scale_factor):
    """
    Takes a tuple (audio_1) and multiplies each value in the tuple by a scalar quantity.
    
    Parameters:
        audio_in(tuple(float)): The input audio as prompted to the user.
        scale_factor(float): A scalar multiplier as prompted to the user.
    Returns:
        tuple(int): The scaled audio after each value within the tuple has been multiplied by the scalar.
    """
    scale_factor = float(scale_factor)
    return tuple(i * scale_factor for i in audio_in)


def add_audios(audio_1, audio_2):
    """
    Adds each value within a tuple to the corresponding value.
    in another tuple to the length of the shorter tuple.

    Parameters:
        audio_1(tuple(float)): The first tuple of audio samples entered after prompting the user.
        audio_2(tuple(float)): The second tuple of audio samples entered after prompting the user.
    Returns:
        combined_audio(tuple(int)): The resultant tuple of audio after the two audios have been added together.
    """
    combined_audio = ()
    if len(audio_1) <= len(audio_2):
        for i in range(len(audio_1)):
            sum_audio = ((float(audio_1[i]) + float(audio_2[i])),)
            combined_audio += sum_audio     
    else:
        for i in range(len(audio_2)):
            sum_audio = ((float(audio_1[i]) + float(audio_2[i])),)
            combined_audio += sum_audio

    return combined_audio
        
def speedup_factor(speedup_multiplier):
    """
    Determines the new playback rate for a sped up audio file as multiplied by a scalar. 
    Parameters:
        speedup_multiplier(float): A scalar multiplier as prompted to the user.
    Returns:
        new_rate(float): The new playback rate for the audio file. 
    """
    speedup_multiplier = float(speedup_multiplier)
    new_rate = speedup_multiplier * 44100
    return new_rate
    

def lowpass_filter(num_samples_to_average, audio):
    """
    Performs a lowpass filter on a tuple of audio samples. This creates a subset of values a set number of values from the first value in the set.
    It then averages all values within this subset and does this from all remaining numbers in the set. Each time a subset is averaged it is appended to the resultant tuple. 
    Parameters:
        num_samples_to_average(int): A user entered value which determines the amount of
        values that will be averaged each time an average is performed in the set.
        audio(tuple(int)): The tuple of audio samples entered after prompting the user.
    Returns:
        lowpass_tuple(tuple(int)): The resultant tuple appended to after lowpass filtering.
    """
    total = 0
    num_samples_to_average = int(num_samples_to_average)
    lowpass_tuple = ()
    for set_number in range(len(audio) - num_samples_to_average + 1):
        for sound in range(num_samples_to_average):
            total += audio[sound + set_number]
        average = total / num_samples_to_average
        lowpass_tuple += (average, )
        total = 0
    return lowpass_tuple

def highpass_filter(num_samples_to_average, audio):
    """
    Performs a highpass filter on a tuple of audio samples.
    This creates a subset of values a set number of values from the first value in the set and makes every second value in this subset the negative of that value.
    It then averages all values within this subset and does this from all remaining numbers in the set. Each time a subset is averaged it is appended to the resultant tuple. 
    Parameters:
        num_samples_to_average(int): A user entered value which determines the amount of
        values that will be averaged each time an average is performed in the set.
        audio(tuple(int)): The tuple of audio samples entered after prompting the user.
    Returns:
        highpass_tuple(tuple(int)): The resultant tuple appended to after highpass filtering.
    """
    total = 0
    num_samples_to_average = int(num_samples_to_average)
    highpass_tuple = ()
    for set_number in range(len(audio) - num_samples_to_average + 1):
        for sound in range(num_samples_to_average):
            if sound % 2 == 0:
                total += audio[sound + set_number]
            else:
                total -= audio[sound + set_number]
        average = total / num_samples_to_average
        highpass_tuple += (average, )
        total = 0
    return highpass_tuple

def mix_audios(audio_1, weight_1, audio_2, weight_2):
    """
    Performs a mixing of audio tuples by first multiplying  each value within two tuples with a corresponding scalar value prompted by the user.
    The function then adds each value of the first audio tuple to each value in the second audio tuple to the length of the shorter tuple.
    Finally, the function rounds each value the resultant tuple to two decimal places.
    Parameters:
        audio_1(tuple(float)): The first tuple of audio samples entered after prompting the user.
        weighted_1(float): The scalar multiple entered by the user for audio_1.
        audio_2(tuple(float)): The second tuple of audio samples entered after prompting the user.
        weighted_2(float): The scalar multiple entered by the user for audio_2.
    Returns:
        rounded_combination(tuple(float)): The tuple of mixed values with each value rounded to two decimal places.
    """
    combination = ()
    weight_1 = float(weight_1)
    weight_2 = float(weight_2)
    weighted_1 = tuple(i * weight_1 for i in audio_1)
    weighted_2 = tuple(i * weight_2 for i in audio_2)
    if len(audio_1) <= len(audio_2):
        for i in range(len(audio_1)):
            sum_audio = ((float(weighted_1[i]) + float(weighted_2[i])),)
            combination += sum_audio     
    else:
        for i in range(len(audio_2)):
            sum_audio = ((float(weighted_1[i]) + float(weighted_2[i])),)
            combination += sum_audio
    rounded_combination = tuple(round(value, 2) for value in combination)
    return rounded_combination
    

def incorrect_response():
    """
    Function to prompt the user to try another command if they enter something incorrect
    Parameters:
    None
    Returns:
    None
    """
    print("Please enter a valid command.")
    main()
    
def indent(text):
    """
    Function to add indentation to strings shown to the user.
    Parameters:
        text(string): The text to be indented.
    Returns:
        text(string): The indented text.
    """
    text = ('    ') + text
    return text


def main():
    """
    Main program function. Gives the options for audio manipulation to the user.
    Takes a string from the user and then splits it by whitespace. Checks if the user entered nothing, prompting the incorrect response function.
    Sets the first object as first letter, a string.
    If the first object was more than one character, prompts the incorrect response function. 
    If the user enters two or more objects split by whitespace, defines the second object as the first number, a float value.
    If the user enters three objects split by white space, check the first letter to see if it's an 'f'. If so, sets the object as the second letter, a string.
    If the second letter does not equal 'l' for lowpass filtering or 'h' for highpass filtering, prints an error message and prompts the user to try again.
    If the third entered object is not an 'f' for audio filtering, this is set to the second number, a float.
    Checks if the first letter is 'c' for changing audio playback speed or 'f'. If so, prompts user to enter an input file name for the audio to be used.
    If the first letter is instead 'm' for mixing audio, the program will prompt the user to enter their first file name as two will be used.
    If the first letter is 'm', 'c', or 'f', whitespace is removed from the users input file name and the read wav file function is called to gather its audio samples and rate.
    If the first letter is 'm', prompts user for the second input file, removing whitespace and reading this file as well using the read wav file function.
    If the first letter is 'm', 'c', or 'f', prompts the user for an output file, removing whitespace from the user entered string.
    Checks if the users first letter was 'q' for quit.
    If so, creates a while loop that forces the user to either enter a 'y' to confirm quitting or an 'n' to back out, or else face a error prompt.
    If a 'y' is entered, the main function is exited, ending the program. Else if 'n' is entered, main is exited, but is then run again.
    If first letter is 'm' writes a new file using write wav file to the output file name by performing the mix audio function on the users entered audio,
    using the sample rate of 44100. Exits the function, restarting main.
    If first letter is 'c' writes a new file using write wav file and the users entered audio.
    The sample rate is changed by the value they specified as first number using the speedup factor function. Exits the function, restarting main.
    If the first letter is 'f', checks if the second letter is 'l' or 'h, and writes the file to the users output file name using the entered audio,
    performing lowpass or highpass filtering respectively at the sample rate of 44100. Exits the function, restarting main.
    If none of these first letters are entered, run the incorrect response function, returning out of the current function.
    Parameters:
        None
    Returns:
        None
    """
    print("Please specify one of the following options:")
    print(indent("'m scale_1 scale_2' Mix two scaled audios together"))
    print(indent("'c integer_speedup_factor' Change the playback speed"))
    print(indent("'f num_samples_to_average l/h' Filter the audio"))
    print(indent("'q' Quit"))
    user_input = input(": ")
    
    split_string = user_input.split()
    if split_string != []:
        first_letter = split_string[0]
    else:
        incorrect_response()
        return
    if len(first_letter) > 1:
        incorrect_response()
        return
    if len(split_string) >= 2:
        first_number = split_string[1]
        float(first_number)
    if len(split_string) == 3:
        if type(split_string[2]) is str and first_letter == "f":
            second_letter = split_string[2]
            if second_letter != "l" and second_letter != "h":
                print("Invalid filter selected, please select lowpass or highpass filtering (l/h).")
                main()
                return
        else:
            second_number = split_string[2]
            float(second_number)
        
    if first_letter == "c" or first_letter == "f":
        file_input_1_name = input("Please enter the input filename: ")
    elif first_letter == "m":
        file_input_1_name = input("Please enter the first input filename: ")
    if first_letter == "c" or first_letter == "f" or first_letter == "m":
        file_input_1_name = ''.join(file_input_1_name.split())
        rate_1, audio_1 = read_wav_file(file_input_1_name)
        
        if first_letter == 'm':
            file_input_2_name = input("Please enter the second input filename: ")
            file_input_2_name = ''.join(file_input_2_name.split())
            rate_2, audio_2 = read_wav_file(file_input_2_name)
        
    
        file_output_name = input("Please enter the output filename: ")
        file_output_name = ''.join(file_output_name.split())
        
    if first_letter == "q":
        while True:
            confirm_quitting = input("Are you sure (y/n): ")
            if confirm_quitting == "y":
                return
            elif confirm_quitting == "n":
                main()
                return
            else:
                print("Please enter a valid command.")
                
    elif first_letter == "m":
        write_wav_file(file_output_name, 44100, mix_audios(audio_1, first_number, audio_2, second_number))
        main()
        return
    elif first_letter == "c":
        write_wav_file(file_output_name, int(speedup_factor(first_number)), audio_1)
        main()
        return
    elif first_letter == "f":
        if second_letter == "l":
            write_wav_file(file_output_name, 44100, lowpass_filter(first_number, audio_1))
            main()
            return
        elif second_letter == "h":
            write_wav_file(file_output_name, 44100, highpass_filter(first_number, audio_1))
            main()
            return
                      
    else:
        incorrect_response()
        return
            
        
                 
        
                        



    



        
        
        
    

    





















