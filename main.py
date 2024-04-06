parodies = [0, 1, 2, 4, 8]
message = [0]*16
error = 0
for i in range(16):
    if i in parodies:
        continue
    else:
        message[i] = int(input())
        if message[i]:
            error ^= i
print(message, error)
for p in parodies:
    if error & p:
        message[p] = 1

for i in range(1, 16):
    message[0] ^= message[i]
print(message)

error_cell = int(input())
message[error_cell] = int(not message[error_cell])
message[2] = int(not message[2])
print(message)

total = 0

error = 0
for i, bit in enumerate(message):
    if bit:
        error ^= i
        total ^= bit

print(bin(error), error)

if error and total:
    message[error] = int(not message[error])
    print(message, error, total)
elif error and not total:
    print("There are two errors!")
else:
    print("No error")

