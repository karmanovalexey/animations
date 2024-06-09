from manim import *


class Conv2d_3_x_3(Scene):
    def construct(self):
        im_size_r = 8
        im_size_c = 8
        sq_size = 0.5
        image = self.create_grid(im_size_r, im_size_c, sq_size)
        image.center()

        conv = self.create_grid(3, 3, sq_size, in_color=GREEN)
        conv.to_edge(LEFT)
        # conv.shift(LEFT)

        self.add(image)
        # self.play(FadeIn(image))

        animations = [Create(square) for square in conv]
        self.play(AnimationGroup(*animations, lag_ratio=0))

        self.play(conv.animate.move_to(UL * 1.75))

        for i in range(im_size_r):
            for j in range(im_size_c):
                self.play(conv.animate.shift(RIGHT * sq_size))
            self.play(conv.animate.shift(LEFT * im_size_c * sq_size + DOWN * sq_size))

        self.wait()

    def create_grid(self, rows, cols, size, in_color=BLACK):
        grid = VGroup()
        
        for i in range(rows):
            for j in range(cols):
                square = Square(side_length=size)
                square.move_to(np.array([i * size, j * size, 0]))
                square.set_fill(in_color, opacity=0.5)  # Set fill color and opacity
                square.set_stroke(WHITE, width=1)  # Optional: Set stroke color and width
                grid.add(square)

        return grid
