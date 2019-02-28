class Setting():
  def __init__(self):
    # 初始化游戏配置
    self.screen_width = 900
    self.screen_height = 600
    self.bg_color = (230, 230, 230)
    self.ship_speed_factor = 1
    # 子弹属性
    self.bullet_speed_factor = 1
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = (60, 60, 60)
    self.bullets_allowed = 3