#Created by: MasterOfficial

#This file includes a class to control DCMOTORS Pololu 70:1 12v

class DCMOTOR:
    def __init__(self, rpwm_d, lpwm_d, rpwm_i, lpwm_i, min_duty=32768, max_duty=65535):
        self.rpwm_d = rpwm_d
        self.lpwm_d = lpwm_d
        self.rpwm_i = rpwm_i
        self.lpwm_i = ipwm_i
        self.min_duty = min_duty
        self.max_duty = max_duty
        
    def forward(self,speed):
        self.speed = speed
        self.rpwm_d.duty_u16(self.duty_cycle(self.speed))
        self.lpwm_d.duty_u16(0)
        self.rpwm_i.duty_u16(self.duty_cycle(self.speed))
        self.lpwm_i.duty_u16(0)
    
    def backwards(self,speed):
        self.speed = speed
        self.rpwm_d.duty_u16(0)
        self.lpwm_d.duty_u16(self.duty_cycle(self.speed))
        self.rpwm_i.duty_u16(0)
        self.lpwm_i.duty_u16(self.duty_cycle(self.speed))
    
    def right(self,speed):
        self.speed = speed
        self.rpwm_d.duty_u16(0)
        self.lpwm_d.duty_u16(self.duty_cycle(self.speed))
        self.rpwm_i.duty_u16(self.duty_cycle(self.speed))
        self.lpwm_i.duty_u16(0)
        
    def left(self,speed):
        self.speed = speed
        self.rpwm_d.duty_u16(self.duty_cycle(self.speed))
        self.lpwm_d.duty_u16(0)
        self.rpwm_i.duty_u16(0)
        self.lpwm_i.duty_u16(self.duty_cycle(self.speed))
        
    def stop(self):
        self.rpwm_d.duty_u16(0)
        self.lpwm_d.duty_u16(0)
        self.rpwm_i.duty_u16(0)
        self.lpwm_i.duty_u16(0)
    
    def duty_cycle(self, speed):
        if self.speed <= 0 or self.speed > 100:
            duty_cycle = 0
        else:
            duty_cycle = int(self.min_duty + (self.max_duty - self.min_duty) * ((self.speed-1)/(100-1)))
        return duty_cycle
