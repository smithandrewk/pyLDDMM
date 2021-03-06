import pyLDDMM
from pyLDDMM.utils.visualization import loadimg, saveimg, save_animation, plot_warpgrid

if __name__ == "__main__":
    # load greyscale images
    i0 = loadimg('./example_images/circle.png')
    i1 = loadimg('./example_images/square.png')

    # perform the registration
    lddmm = pyLDDMM.LDDMM2D()
    im, v, energies, length, Phi0, Phi1, J0, J1 = lddmm.register(i0, i1, sigma=0.1, alpha=1, epsilon=0.0001, K=20)

    # save i0 aligned to i1
    saveimg('./example_images/out_c2s.png', im)

    # save animation of the transformation
    save_animation('./example_images/out_c2s.gif', J0)

    # plot the transfomration
    plt = plot_warpgrid(Phi1[0], interval=1)
    plt.savefig('./example_images/out_c2s_warp.png')