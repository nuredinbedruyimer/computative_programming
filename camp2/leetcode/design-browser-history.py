class BrowserHistory:
  def __init__(self, homepage: str):
    self.urls = []
    self.start_index = -1
    self.last_index = -1
    self.visit(homepage)

  def visit(self, url: str) -> None:
    self.start_index+= 1
    if self.start_index < len(self.urls):
      self.urls[self.start_index] = url
    else:
      self.urls.append(url)
    self.last_index = self.start_index

  def back(self, steps: int) -> str:
    self.start_index = max(0, self.start_index - steps)
    return self.urls[self.start_index]

  def forward(self, steps: int) -> str:
    self.start_index = min(self.last_index, self.start_index + steps)
    return self.urls[self.start_index]