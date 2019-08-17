from .game import AsciiRacer
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def main():
    # Example for how to use asciiracer class as an agent
    asciiracer = AsciiRacer()
    matrices = []
    for x in range(1000):
        score, matrix = asciiracer.step(ord('w'))
        matrices.append(matrix)
    asciiracer.step(ord('q'))
    animate(matrices)


def animate(movie):
    fig = plt.figure()
    ims = []
    for image in movie:
        im = plt.imshow(image, animated=True)
        ims.append([im])
    _ = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                  repeat_delay=1000)
    plt.show()


main()
