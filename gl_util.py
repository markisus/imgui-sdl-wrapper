import OpenGL.GL as gl

class GlRgbTexture:
    def __init__(self, width, height):
        self.width = 0
        self.height = 0
        self.texture_id = 0
        self.have_data = False
        self.setup(width, height)
    
    def setup(self, width, height):
        self.width = width
        self.height = height

        self.texture_id = gl.glGenTextures(1)
        gl.glBindTexture(gl.GL_TEXTURE_2D, self.texture_id)
        gl.glPixelStorei(gl.GL_UNPACK_ALIGNMENT, 1)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)

        gl.glBindTexture(gl.GL_TEXTURE_2D, 0)

    def update(self, data):
        gl.glBindTexture(gl.GL_TEXTURE_2D, self.texture_id)

        if not self.have_data:
            gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB,
                            self.width, self.height, 0, gl.GL_RGB,
                            gl.GL_UNSIGNED_BYTE, data)
            self.have_data = True
        else:
            gl.glTexSubImage2D(gl.GL_TEXTURE_2D,
                               0, 0, 0,
                               self.width, self.height,
                               gl.GL_RGB,
                               gl.GL_UNSIGNED_BYTE,
                               data)

        gl.glBindTexture(gl.GL_TEXTURE_2D, 0)

        
    def __del__(self):
        gl.glDeleteTextures(1, [self.texture_id])
