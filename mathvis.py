import numpy as np


def generate_contour(mu, cov, radius=1, num_points=360):
    """ Generates PDF contour points for a bivariate normal distribution

    :param mu:         distribution mean
    :type  mu:         (2, ) or (2, 1) numpy.ndarray
    :param cov:        distribution covariance
    :type  cov:        (2, 2) numpy.ndarray
    :param radius:     contour size param, num of standard deviations, opt
    :type  radius:     positive float
    :param num_points: num of points to generate, evenly-spaced in radians, opt
    :type  num_points: positive int
    :return:           x and y values lying on a PDF contour
    :rtype:            (2, num_points) np.ndarray
    """
    if len(mu.shape) == 1:
        mu = mu[:, np.newaxis]
    eigval, eigvec = np.linalg.eig(cov)

    # first make a circle
    theta = np.linspace(0, 2 * np.pi, 360)
    x_circ, y_circ = radius * np.cos(theta), radius * np.sin(theta)

    # stretch circle to ellipse and rotate, in accordance with the covariance
    x_elli, y_elli = eigval[0] * x_circ, eigval[1] * y_circ
    contour = eigvec @ np.stack([x_elli, y_elli], axis=0)

    # shift resulting ellipse by distribution mean (loc)
    contour += mu
    return contour
