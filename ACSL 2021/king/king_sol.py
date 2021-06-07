# Row
def rowCheck(rLoc, cLoc, occupied, unsafe_positions):
    ranges = [range(cLoc + 1, 8), range(cLoc - 1, -1, -1)]
    for rg in ranges:
        for c in rg:
            unsafe_positions.add((rLoc, c))
            if (rLoc, c) in occupied: break

# Column
def colCheck(rLoc, cLoc, occupied, unsafe_positions):
    ranges = [range(rLoc + 1, 8), range(rLoc - 1, -1, -1)]
    for rg in ranges:
        for r in rg:
            unsafe_positions.add((r, cLoc))
            if (r, cLoc) in occupied: break

# / Diagonal
def forwardDiagCheck(rLoc, cLoc, occupied, unsafe_positions):
    ranges = [range(rLoc + 1, 8), range(rLoc - 1, -1, -1)]
    for rg in ranges:
        for r in rg:
            unsafe_positions.add((r, rLoc + cLoc - r))
            if (r, rLoc + cLoc - r) in occupied: break

# \ Diagonal
def backDiagCheck(rLoc, cLoc, occupied, unsafe_positions):
    ranges = [range(rLoc + 1, 8), range(rLoc - 1, -1, -1)]
    for rg in ranges:
        for r in rg:
            unsafe_positions.add((r, r + cLoc - rLoc))
            if (r, r + cLoc - rLoc) in occupied: break

def find_king_status(pieces):
    pieces = pieces.strip(" ").strip("\n").split(" ")
    unsafe_positions = set()
    kingLoc = (0, 0)
    alphaNum = {"abcdefgh"[i]:i for i in range(8)}
    positionValid = lambda r, c: 0 <= r < 8 and 0 <= c < 8
    occupied = set()
    for piece in pieces:
        pieceType, rLoc, cLoc = piece[0], 8 - int(piece[2]), alphaNum[piece[1]]
        if pieceType == "K": continue
        occupied.add((rLoc, cLoc))

    for piece in pieces:
        pieceType, rLoc, cLoc = piece[0], 8-int(piece[2]), alphaNum[piece[1]]
        if pieceType == "K":
            kingLoc = (rLoc, cLoc)
            continue
        elif pieceType == "Q":
            # check for unsafe positions in row, col, / diag, \ diag
            rowCheck(rLoc, cLoc, occupied, unsafe_positions)
            colCheck(rLoc, cLoc, occupied, unsafe_positions)
            forwardDiagCheck(rLoc, cLoc, occupied, unsafe_positions)
            backDiagCheck(rLoc, cLoc, occupied, unsafe_positions)
        elif pieceType == "R":
            # check for unsafe positions in row, col
            rowCheck(rLoc, cLoc, occupied, unsafe_positions)
            colCheck(rLoc, cLoc, occupied, unsafe_positions)
        elif pieceType == "B":
            # check for unsafe positions in / diag, \ diag
            forwardDiagCheck(rLoc, cLoc, occupied, unsafe_positions)
            backDiagCheck(rLoc, cLoc, occupied, unsafe_positions)
        elif pieceType == "P":
            unsafe_positions.add((rLoc-1, cLoc-1))
            unsafe_positions.add((rLoc-1, cLoc+1))
        elif pieceType == "N":
            knightDirs = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
            for k in knightDirs:
                unsafe_positions.add((rLoc+k[0], cLoc+k[1]))
    # Check for four possible states of king
    kingCanMove = False
    for dR in [-1, 0, 1]:
        for dC in [-1, 0, 1]:
            nR, nC = kingLoc[0]+dR, kingLoc[1]+dC
            if not positionValid(nR, nC) or (dR == 0 and dC == 0): continue
            if (nR, nC) not in unsafe_positions:
                kingCanMove = True
                break
        else: continue
        break
    kingSafeCurrently = kingLoc not in unsafe_positions
    if kingSafeCurrently and kingCanMove: return "SAFE"
    elif kingSafeCurrently and not kingCanMove: return "STALEMATE"
    elif not kingSafeCurrently and kingCanMove: return "CHECK"
    else: return "CHECKMATE"
