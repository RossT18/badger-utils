from badger2040 import WIDTH, HEIGHT

class API:
  def __init__(self, display):
    self.display = display

  def clear_screen(self):
    self.display.set_pen(15) # white
    self.display.clear()
    self.display.set_pen(0) # return to black pen

  def find_font_height(self, font_name, scale=1):
    bitmap_fonts = {'bitmap6': 6, 'bitmap8': 8, 'bitmap14_outline': 14}
    if font_name in bitmap_fonts:
      return bitmap_fonts[font_name] * scale
    else:
      return scale * 20
      # TODO: Measure vector fonts properly
      # From the docs:
      # At scale=1, the top edge of upper case letters is 10 pixels above the specified y,
      # text baseline is 10 pixels below the specified y,
      # and descenders go down to 20 pixels below the specified y.

  def draw_text(self, user_text_properties):
    default_text_properties = {
      'text': '',
      'scale': 1,
      'x': 0,
      'y': 0,
      'max_width': WIDTH,
      'font': 'bitmap8',
      'colour': 0, # 0 (black) to 15 (white)
      'horizontal_align': 'left', # left or right. If right, x position is subtracted from display width and width of text
      'vertical_align': 'top', # top or bottom
    }
    text_props = {}
    text_props.update(default_text_properties)
    text_props.update(user_text_properties)

    self.display.set_pen(text_props['colour'])
    self.display.set_font(text_props['font'])

    text_width = self.display.measure_text(text_props['text'], text_props['scale'])
    text_height = self.find_font_height(text_props['font'], text_props['scale'])

    if text_props['horizontal_align'] == 'right':
      text_props.update({ 'x': WIDTH - text_width - text_props['x'] })
    if text_props['vertical_align'] == 'bottom':
      text_props.update({ 'y': HEIGHT - text_height - text_props['y'] })

    self.display.text(
      text_props['text'],
      text_props['x'],
      text_props['y'],
      text_props['max_width'],
      text_props['scale'],
    )

    return (text_width, text_height)
