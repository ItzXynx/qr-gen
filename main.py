import sys

def fake_qr(text):
    import hashlib
    h = hashlib.md5(text.encode()).hexdigest()
    size = 17
    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            if (i < 6 and j < 6) or (i < 6 and j > size-7) or (i > size-7 and j < 6):
                row.append(1 if (i==0 or i==5 or j==0 or j==5 or (2<=i<=3 and 2<=j<=3)) else 0)
            else:
                idx = (i * size + j) % len(h)
                row.append(int(h[idx], 16) % 2)
        grid.append(row)
    return "\n".join("".join("██" if c else "  " for c in row) for row in grid)

if __name__ == "__main__":
    text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "hello"
    print(f"\n{fake_qr(text)}\n")
    print(f"content: {text}")
# updated
