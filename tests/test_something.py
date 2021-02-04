import pytest
import Sword


def test_modules_empty():
    mgr = Sword.SWMgr("/tmp")
    modules = mgr.getModules()
    assert modules.size() == 0
