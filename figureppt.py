import io
import pptx


class FigurePptSink:
    def __init__(self, height=7.5, width=10):
        """ Constructor

        :param height: presentation height in inches, optional
        :type  height: positive float
        :param width: presentation width in inches, optional
        :type  width: positive float
        """
        self.buffer = io.BytesIO()
        ppt = pptx.Presentation()
        ppt.slide_height = pptx.util.Inches(height)
        ppt.slide_width = pptx.util.Inches(width)
        self.ppt = ppt

    def add_slide(self, fig):
        """ Append figure to running slide deck

        :param fig: figure to add
        :type  fig: matplotlib.pyplot.Figure
        """
        fig.savefig(self.buffer)  # load image into buffer
        slide = self.ppt.slides.add_slide(self.ppt.slide_layouts[6])  # +blank
        slide.shapes.add_picture(
            self.buffer,
            left=pptx.util.Inches(0),
            top=pptx.util.Inches(0))  # add image to slide from buffer
        self.buffer.seek(0)  # move buff pointer to buff start
        self.buffer.truncate()  # clear image from buffer

    def save(self, filepath):
        """ Save running slide deck to disk

        :param filepath: target path on disk
        :type  filepath: str
        """
        self.ppt.save(filepath)
