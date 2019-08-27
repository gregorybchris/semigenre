from semigenre.audio.player import Player


def test_play(playable_track):
    p = Player(playable_track)
    p.play()
    p.stop()


def test_pause_resume(playable_track):
    p = Player(playable_track)
    p.play()
    p.pause()
    p.resume()
    p.stop()


def test_forward_rewind(playable_track):
    p = Player(playable_track)
    p.play()
    p.forward()
    p.rewind()
    p.stop()


def test_get_state(playable_track):
    p = Player(playable_track)
    p.play()
    assert p.get_state() == Player.PLAY
    p.stop()
