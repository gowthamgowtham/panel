from typing import Any

from bokeh.core.properties import Bool, Readonly
from bokeh.events import ModelEvent

from ..io.resources import bundled_files
from ..util import classproperty
from .layout import Column

__all__ = (
    "Modal",
    "ModalDialogEvent",
)


class Modal(Column):

    __javascript_raw__ = [
        "https://cdn.jsdelivr.net/npm/a11y-dialog@7/dist/a11y-dialog.min.js"
    ]

    @classproperty
    def __javascript__(cls):
        return bundled_files(cls)

    @classproperty
    def __js_skip__(cls):
        return {'A11yDialog': cls.__javascript__[:1]}

    __js_require__ = {
        'paths': {
            'a11y-dialog': "https://cdn.jsdelivr.net/npm/a11y-dialog@7/dist/a11y-dialog.min",
        },
        'exports': {
            'A11yDialog': 'a11y-dialog',
        }
    }

    is_open = Readonly(Bool, default=False, help="Whether or not the modal is open.")
    show_close_button = Bool(True, help="Whether to show a close button in the modal.")
    background_close = Bool(True, help="Whether to enable closing the modal when clicking the background.")


class ModalDialogEvent(ModelEvent):
    event_name = 'modal-dialog-event'

    def __init__(self, model: ModelEvent, open: bool):
        self.open = open
        super().__init__(model=model)

    def event_values(self) -> dict[str, Any]:
        return dict(super().event_values(), open=self.open)
