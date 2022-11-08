def contents_change(self, position, charsRemoved, charsAdded):
    if not self.area_for_typing.document().toPlainText():
        return
    if len(self.area_for_typing.document().toPlainText()) == 1:
        self.seconds = 0
        self.current_wpm = 0
        self.accuracy_per = 0
        self.timer.start(1000)

    cursor = self.text_for_typing.textCursor()
    cursor.setPosition(position)
    end = cursor.movePosition(QTextCursor.NextCharacter, 1)
    self.text = self.text_for_typing.toPlainText()

    try:
        if end:
            letter_text = self.text[position]
            letter_area_for_typing = self.area_for_typing.document().toPlainText()[position]
            if letter_text == letter_area_for_typing:
                self.format.setTextOutline(QPen(QColor("green")))
            else:
                self.format.setTextOutline(QPen(QColor("red")))
    except:
        pass
    cursor.mergeCharFormat(self.format)