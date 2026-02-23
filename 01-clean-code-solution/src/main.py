import sys

def is_lock(block: list[str]):
    first_line = block[0]
    last_line = block[-1]

    return (
            first_line.count("#") == len(first_line)
            and last_line.count(".") == len(last_line)
    )

def heights_lock(block):
    w = len(block[0])
    h = len(block)
    res = []
    for c in range(w):
        k = 0
        for r in range(h):
            if block[r][c] == "#":
                k += 1
            else:
                break
        res.append(max(0, k - 1))
    return res, h

def heights_key(block):
    w = len(block[0])
    h = len(block)
    res = []
    for c in range(w):
        k = 0
        for r in range(h - 1, -1, -1):
            if block[r][c] == "#":
                k += 1
            else:
                break
        res.append(max(0, k - 1))
    return res, h


def main():
    lines = [l.rstrip("\n") for l in sys.stdin.read().splitlines()]

    blocks = []
    cur = []
    for l in lines:
        if l.strip() == "":
            if cur:
                blocks.append(cur)
                cur = []
        else:
            cur.append(l)
    if cur:
        blocks.append(cur)

    locks = []
    keys = []

    for b in blocks:
        if not b:
            continue
        if is_lock(b):
            hv, hh = heights_lock(b)
            locks.append((hv, hh))
        else:
            hv, hh = heights_key(b)
            keys.append((hv, hh))

    ans = 0
    for lh, hL in locks:
        for kh, hK in keys:
            H = min(hL, hK)
            ok = True
            for i in range(len(lh)):
                if lh[i] + kh[i] > H - 2:
                    ok = False
                    break
            if ok:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
