from manim import *
class MatrixTransform(LinearTransformationScene):
    def __init__(self, **kwargs):
      super().__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            **kwargs
        )

    def construct(self):
         matrix=[[1,0],
                 [1,0]]
         self.apply_matrix(matrix)
         self.wait()
