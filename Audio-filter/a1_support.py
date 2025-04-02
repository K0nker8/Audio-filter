from scipy.io.wavfile import read, write
import numpy as np


HELP_MSG = """Please specify one of the following options:
    'm scale_1 scale_2' Mix two scaled audios together
    'c integer_speedup_factor' Change the playback speed
    'f num_samples_to_average l/h' Filter the audio
    'q' Quit
: """


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
