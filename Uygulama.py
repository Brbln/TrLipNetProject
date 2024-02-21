from PIL import Image
import os

def combine_frames(frames, canvas_size):
    combined_image = Image.new("RGBA", canvas_size)

    x_offset, y_offset = 0, 0
    for frame in frames:
        combined_image.paste(frame, (x_offset, y_offset))
        x_offset += frame.width
        if x_offset >= canvas_size[0]:
            x_offset = 0
            y_offset += frame.height

    return combined_image

def combine_gif_frames(gif_path, output_directory):
    output_size = (720,720)
    
    # GIF'i aç
    gif = Image.open(gif_path)
    frames = []

    try:
        while True:
            frame = gif.convert("RGBA")
            frames.append(frame)
            gif.seek(gif.tell() + 1)
    except EOFError:
        pass

    while len(frames) < 49:
        frames.append(frames[-1])

    if len(frames) > 49:
        frames = frames[-49:]

    while len(frames) < 49:
        frames.append(frames[-1])
        
    num_frames = len(frames)
    num_per_row = int(num_frames ** 0.5)
    width = num_per_row * frames[0].width
    height = (num_frames // num_per_row) * frames[0].height

    combined_image = combine_frames(frames, (width, height))
    combined_image_resized = combined_image.resize(output_size)

    gif_basename = os.path.splitext(os.path.basename(gif_path))[0]
    combined_image_filename = gif_basename + ".png"
    combined_image_path = os.path.join(output_directory, combined_image_filename)
    os.makedirs(output_directory, exist_ok=True)

    combined_image_resized.save(combined_image_path)

    return combined_image_path


def process_gif_directory(input_directory, output_directory):
    gif_files = [f for f in os.listdir(input_directory) if f.lower().endswith('.gif')]

    for gif_file in gif_files:
        gif_path = os.path.join(input_directory, gif_file)
        combine_gif_frames(gif_path, output_directory)

input_gif_directory = "C:/Users/abrbl/VeriSeti/_veri/sonGif/RenkliGif/Nasilsin"
output_directory = "C:/Users/abrbl/VeriSeti/_veri/BirlesikGifler1/Nasilsin"

process_gif_directory(input_gif_directory, output_directory)
