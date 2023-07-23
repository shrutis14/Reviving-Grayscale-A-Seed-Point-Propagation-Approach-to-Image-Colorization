import cv2
import numpy as np
import itertools

from artifact_removal.core.filter import GuidedFilter
from artifact_removal.tools import visualize as vis
from artifact_removal.cv.image import to_8U, to_32F
from PIL import Image as im

def test_color():
    image = cv2.imread('output.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #cv2.imshow("Image", image)
    cv2.waitKey(0)
    noise = (np.random.rand(image.shape[0], image.shape[1], 3) - 0.5) * 50
    image_noise = image + noise

    radius = [15]
    eps = [0.005]

    combs = list(itertools.product(radius, eps))
    #vis.plot_single(to_32F(image), title='origin')
    #vis.plot_single(to_32F(image_noise), title='noise')

    for r, e in combs:
        GF = GuidedFilter(image, radius=r, eps=e)
        #vis.plot_single(to_32F(GF.filter(image_noise)), title='r=%d, eps=%.3f' % (r, e))
        #print(type(to_32F(GF.filter(image_noise))))
        arr = (to_32F(GF.filter(image_noise)) * 255).astype(np.uint8)
        img = im.fromarray(arr)
        #img.show()
        img.save("filter.png")
#if __name__ == '__main__':
    #test_color()
