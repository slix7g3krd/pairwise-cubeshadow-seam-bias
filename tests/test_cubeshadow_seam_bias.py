import pytest
import graphics.cubeshadow_seam_bias as mod

CASES = [
    ("face_guard", (1,)),
    ("slope_bias", (1,)),
    ("all_faces_barrier", (1,)),
    ("per_face_invalidate", (1,)),
    ("light_id_slot", (1,)),
    ("recycle_slot", (1,)),
    ("render_faces", (1,)),
    ("bind_cube", (1,)),
    ("sample", (1,)),
    ("move_light", (1,)),
    ("validate_seam", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
