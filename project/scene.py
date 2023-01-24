from manim import *


class CreateCircle(Scene):

    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class SquareToCircle(Scene):

    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square,
                            circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation


class SquareAndCircle(Scene):

    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen


class AnimatedSquareToCircle(Scene):

    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(ReplacementTransform(
            square, circle))  # transform the square into a circle
        self.play(circle.animate.set_fill(
            PINK, opacity=0.5))  # color the circle on screen


class HelloLaTeX(Scene):

    def construct(self):
        tex = Tex(r"\LaTeX", font_size=144)
        self.add(tex)


class DifferentRotations(Scene):

    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(left_square.animate.rotate(PI / 4),
                  Rotate(right_square, angle=PI / 4),
                  run_time=2)
        self.wait()


class ManimCELogo(Scene):

    def construct(self):
        self.camera.background_color = "#ece6e2"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.move_to(ORIGIN)
        self.add(logo)


class GradientImageFromArray(Scene):

    def construct(self):
        n = 256
        imageArray = np.uint8([[i * 256 / n for i in range(0, n)]
                               for _ in range(0, n)])
        for i in range(0, n):
            imageArray[i][0] = 255
        imageArray[0] = [255 for i in range(0, n)]
        imageArray[n - 1] = [255 for i in range(0, n)]
        image = ImageMobject(imageArray).scale(3)
        self.add(image)


class Coordinate(Scene):

    def construct(self):
        np = NumberPlane()
        o_dot = Dot(ORIGIN)
        x_dot = Dot([2, 2, 0])
        arrow = Arrow(o_dot, x_dot, buff=0)
        o_text = Text('(0,0)').next_to(o_dot, DOWN)
        x_text = Text('(2,2)').next_to(x_dot, RIGHT)
        img = ImageMobject('./assets/风景.png')
        img.shift(3 * LEFT + 2 * UP)
        self.add(img)
        self.add_sound('./assets/kiss the rain.mp3')
        self.play(Create(np))
        self.play(FadeIn(o_dot))
        self.play(Write(o_text))
        self.wait()
        self.play(Write(arrow))
        self.play(Create(x_dot))
        self.play(Write(x_text))
        self.play(Rotate(arrow, 3 * PI / 4, about_point=[0, 0, 0]))
        self.wait()
