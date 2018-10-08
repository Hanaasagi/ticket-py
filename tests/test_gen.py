from __future__ import absolute_import

import ticket


def test_unique(benchmark):
    ticketing = ticket.Ticketing()
    id_1 = benchmark(ticketing.gen)
    id_2 = ticketing.gen()
    assert id_1 != id_2


def test_encode(benchmark):
    id_s = benchmark(ticket.encode, [91, 168, 192, 19, 123, 235, 192, 25, 161, 153, 245, 249])  # noqa
    assert id_s == "bekc04rrtf01j8cpunsg"


def test_decode(benchmark):
    id_raw = benchmark(ticket.decode, "bekc04rrtf01j8cpunsg")
    assert id_raw == [91, 168, 192, 19, 123, 235, 192, 25, 161, 153, 245, 249]  # noqa


def test_threadsafe():
    import threading

    ticketing = ticket.Ticketing()
    result = [None] * 10

    def g(result, i):
        result[i] = ticket.encode(ticketing.gen())

    threads = []
    for i in range(10):
        t = threading.Thread(target=g, args=(result, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    assert len(set(result)) == 10
