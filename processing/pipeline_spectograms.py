import pathlib
import re

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment
from tqdm import tqdm

from processing.data_management import get_genres, remove_and_create_empty_directory

from config.paths import MP3, SPECTROGRAMS, WAV

MS_ADJUSTMENT = 1000


def generate_wav_samples(sample_size: int = 1000) -> None:

    _, genres = get_genres(MP3)

    for genre in genres:
        genre_path = MP3 / genre
        files = [file_name for file_name in genre_path.iterdir()]
        remove_and_create_empty_directory(WAV/genre)
        print(f"Generating samples for {genre}")
        for i in range(len(files)):
            print(f"Generating samples from file {i + 1}")
            current_file = files[i]
            song = AudioSegment.from_mp3(current_file)
            song.set_channels(1)
            length_song = song.duration_seconds
            samples = length_song * np.random.sample(size=sample_size)
            for j in tqdm(range(sample_size)):
                start = samples[j] * MS_ADJUSTMENT
                end = start + 5 * MS_ADJUSTMENT
                sample_song = song[start:end]
                output_path = WAV / genre / (genre + f"_{i + 1}_{j + 1}.wav")
                sample_song.export(out_f=output_path, format="wav")


def generate_spectograms() -> None:
    _, genres = get_genres(WAV)
    for genre in genres:
        genre_path = WAV / genre
        files = [file_name for file_name in genre_path.iterdir()]
        remove_and_create_empty_directory(SPECTROGRAMS/genre)
        print(f"Generating samples for {genre}")
        for file_n in tqdm(files):
            re_name = re.compile(f"(?<=_)(.*)(?=.wav)")
            index = re_name.search(file_n.as_posix()).group(1)
            output_path = SPECTROGRAMS / genre / (genre + f"_{index}.png")
            create_spectrogram(file_n, output_path)


def create_spectrogram(input_path: str, output_path: str) -> None:
    plt.interactive(False)
    clip, sample_rate = librosa.load(input_path, sr=None)
    fig = plt.figure(figsize=[1, 1])
    ax = fig.add_subplot(111)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    S = librosa.feature.melspectrogram(y=clip, sr=sample_rate)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    filename = pathlib.Path(output_path)
    plt.savefig(filename, dpi=400, bbox_inches="tight", pad_inches=0)
    plt.close()
    fig.clf()
    plt.close(fig)
    plt.close("all")


if __name__ == "__main__":
    generate_spectograms()
