import sqlalchemy as sa
from sqlalchemy.engine.url import make_url
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy.util import get_cls_kwargs

from source.default_model import get_default_model_class
from source.default_meta import DefaultMeta
from source.session_proxy import SessionProxy


class SQLAlchemy(SessionProxy):
    def __init__(self,
                 url="sqlite://",
                 *,
                 metadata=None,
                 metaclass=None,
                 model_class=None,
                 scopefunc=None,
                 **options):
        self.url = url
        self.info = make_url(url)
        self.Model = self._make_declarative_base(model_class, metadata,
                                                 metaclass)

        self._set_session_options(options)
        self.engine = sa.create_engine(url, **self.engine_options)
        self.Session = sessionmaker(bind=self.engine, **self.session_options)
        self._session = scoped_session(self.Session, scopefunc)

        _include_sqlalchemy(self)

    def _set_session_options(self, options):
        session_options = {}

        for arg in get_cls_kwargs(Session):
            if arg in options:
                session_options[arg] = options.pop(arg)

        options.setdefault("echo", False)
        self.engine_options = options

        session_options.setdefault("autoflush", True)
        session_options.setdefault("autocommit", False)
        self.session_options = session_options

    def _make_declarative_base(self,
                               model_class,
                               metaclass=None,
                               metadata=None):
        """Creates the declarative base."""
        return declarative_base(
            name="Model",
            cls=model_class or get_default_model_class(self),
            metaclass=metaclass or DefaultMeta,
            metadata=metadata,
        )

    @property
    def metadata(self):
        """Proxy for ``Model.metadata``."""
        return self.Model.metadata

    def create_all(self, *args, **kwargs):
        """Creates all tables."""
        kwargs.setdefault("bind", self.engine)
        self.Model.metadata.create_all(*args, **kwargs)

    def drop_all(self, *args, **kwargs):
        """Drops all tables."""
        kwargs.setdefault("bind", self.engine)
        self.Model.metadata.drop_all(*args, **kwargs)

    def reconfigure(self, **kwargs):
        """Updates the session options."""
        self._session.remove()
        self.session_options.update(**kwargs)
        self._session.configure(**self.session_options)

    def __repr__(self):
        return "<SQLAlchemy('{}')>".format(self.url)


def _include_sqlalchemy(obj):
    for module in sa, sa.orm:
        for key in module.__all__:
            if not hasattr(obj, key):
                setattr(obj, key, getattr(module, key))
    obj.event = sa.event
