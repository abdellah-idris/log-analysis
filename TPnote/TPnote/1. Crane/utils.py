import re
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.animation import FuncAnimation

def extract_marker_coordinates(line):
    marker_pattern = r"m[1-3]:\s*\((\d+),(\d+)\)"
    matches = re.findall(marker_pattern, line)
    marker_coordinates = [(int(x), int(y)) for x, y in matches]
    return marker_coordinates

def plot_marker_movement(filename):
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)  # Adjust the bottom margin to accommodate the slider

    with open(filename, "r") as file:
        lines = file.readlines()

    timestamps = [i for i in range(len(lines))]  # Create timestamps for each line
    marker_data = {f"m{i + 1}": {'x': [], 'y': []} for i in range(3)}  # Initialize marker data
    markers_valid = []  # List to store MarkersValid values

    # Extract marker coordinates and update marker data
    for line in lines:
        marker_coordinates = extract_marker_coordinates(line)
        markers_valid.append(re.search(r'MarkersValid:\s*(\w+)', line).group(1))  # Extract MarkersValid value
        for i, (x, y) in enumerate(marker_coordinates):
            marker_data[f"m{i + 1}"]['x'].append(x)
            marker_data[f"m{i + 1}"]['y'].append(y)

    ax.set_xlabel("Position X")
    ax.set_ylabel("Position Y")
    ax.grid(True)

    axcolor = 'lightgoldenrodyellow'
    ax_slider = plt.axes([0.1, 0.05, 0.65, 0.03], facecolor=axcolor)
    slider = Slider(ax_slider, 'Line', 0, len(lines) - 1, valinit=0, valstep=1)

    def update(val):
        line_index = int(slider.val)
        ax.clear()
        ax.set_xlim(0, 150000)  # Adjust x-axis limits
        ax.set_ylim(0, 150000)  # Adjust y-axis limits
        for marker, data in marker_data.items():
            ax.plot(data['x'][line_index], data['y'][line_index], marker='o', linestyle='-', label=marker)
        ax.legend()
        ax.set_title(f"Movement des Marqueurs - {filename} - Line {line_index + 1}, MarkersValid: {markers_valid[line_index]}")

    slider.on_changed(update)

    def animate_graph(frame):
        slider.set_val(frame)

    # Animate the graph using FuncAnimation with a faster interval (100 milliseconds)
    anim = FuncAnimation(fig, animate_graph, frames=len(lines), interval=500)

    plt.show()
