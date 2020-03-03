def find_missing_letter(chars):
    abcs = "abcdefghijklmnopqrstuvwxyz"
    comp = abcs[abcs.index(chars[0].lower()):abcs.index(chars[0].lower())+len(chars)]
    for ind,ch in enumerate(chars):
          if ch.lower() != comp[ind].lower():
              if ch.islower():
                  return comp[ind]
              else:
                  return comp[ind].upper()
              break

