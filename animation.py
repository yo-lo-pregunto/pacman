from constants import ANIMATION_FRAME_RATE as RATE

class Animation():
    def __init__(self, start: int, frames: list[int],
                 speed: int = RATE) -> None:
        self.frame = start
        self.frames = frames
        self.frame_timer = 0
        self.speed = speed
        self.start = start

    def reset(self):
        self.frame = self.start
        self.frame_timer = 0

    def get_frame(self) -> int:
        self.frame_timer += 1
        if self.frame_timer < self.speed:
            return self.frame
        
        self.frame_timer = 0
        self.frame += 1
        if self.frame == len(self.frames):
            self.frame = 0

        return self.frame
