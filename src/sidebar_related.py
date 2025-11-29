class Links():
    def __init__(self,
                 links: list[str],
                 titles: list[str]):
        if len(links) != len(titles): raise Exception()
        self.data = [(l, t) for l, t in zip(links, titles)]
    
    def get(self):
        return ", ".join([f'<a class="sidebar-text" href="{l}">{t}</a>' for l, t in self.data])

class Head:
    def __init__(self, head: str):
        self.head = head
    def get(self) -> str:
        return f'<div class="borderline-spacer-sidebar sidebar-mtr sidebar-title-one" style="margin-top:8%;">{self.head}</div>'
    
class Title:
    def __init__(self, title: str):
        self.title = title
    def get(self) -> str:
        return f'<div class="sidebar-mtr sidebar-title-two more-weight" style="margin-top:4%;">{self.title}</div>'

class Content:
    def __init__(self, content: str):
        self.content = content
    def get(self) -> str:
        return f'<div><p class="sidebar-mtr sidebar-text">{self.content}</p></div>'