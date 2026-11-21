import csv

# questions:
    # aggregate- how much time did I spend knitting in total
    # grouped- How many times did I knit more than 1 new row
    # most frequent- What was the most common type of row (cable or normal)
    # min/max- what was the most and least amount of stitches done at a time
    # custom- About how many stitches are in a row
    # custom- how many stitches per minute when row type is not a cable row

# should be 5052 total stitches, 28 total rows, 7 times knit more than one row,
# total time should be 425:38, 72 least stitches and 457 most stitches, 
# about 180 stitches per row, and around 13 stitches per minute while not cabling
total_stitches = 0
total_rows = 0
least_knit = 0
most_knit = 0
time = ''
total_seconds = 0
total_time = ''
total_hours = 0
total_stitches_nocable = 0
nocable_seconds = 0
sts_per_minute = ''
new_row_count = 0
normal_row_count = 0
cable_row_count = 0

with open("mydata.csv", "r") as data:
    rows = csv.DictReader(data)
    for row in rows:
        #print(row)
        total_stitches += int(row["stitches"])
        total_rows += int(row["newrows"])
        stitches_per_row = total_stitches // total_rows

        #least and most knit
        if least_knit == 0:
            least_knit = total_stitches
        elif least_knit > int(row["stitches"]):
            least_knit = int(row["stitches"])
        if most_knit < int(row["stitches"]):
            most_knit = int(row["stitches"])

        #times knit more than one row
        if int(row["newrows"]) > 1:
            new_row_count += 1

        #time 
        time = row["time"]
        if len(time) == 4:
            total_seconds += int(time[0])*60 + int(time[2] + time[3])
        elif len(time) == 5:
            total_seconds += int(time[0] + time[1])*60 + int(time[3] + time[4])
        total_time = str(total_seconds//60) + ":" + str(total_seconds % 60)
        total_hours = total_seconds//60//60

        #sts per minute when not cabling
        if row["cablerow"] == "False":
            total_stitches_nocable += int(row["stitches"])

        if len(time) == 4 and row["cablerow"] == "False":
            nocable_seconds += int(time[0])*60 + int(time[2] + time[3])
        elif len(time) == 5 and row["cablerow"] == "False":
            nocable_seconds += int(time[0] + time[1])*60 + int(time[3] + time[4])
        sts_per_minute = total_stitches_nocable//(nocable_seconds//60)

        #row type frequency
        if row["cablerow"] == "False":
            normal_row_count += 1
        elif row["cablerow"] == "True":
            cable_row_count += 1


print(f"How much time did I spend knitting in total? {total_time} minutes/{total_hours} hours.")
print(f"How many times did I knit more than 1 new row? {new_row_count}.")
if normal_row_count > cable_row_count:
    print("What was the most common type of row? Normal row")
else:
    print("What was the most common type of row? Cable row")
print(f"What was the most amount of stitches done at a time? {most_knit}")
print(f"What was the least amount of stitches done at a time? {least_knit}")
print(f"What was the average amount of stitches per row? {stitches_per_row}")
print(f"How many stitches per minute when the row was not a cable row? {sts_per_minute}")

#print(sts_per_minute)
#print(stitches_per_row)
#print(normal_row_count)
#print(cable_row_count)
#print(new_row_count)
#print(total_time)
#print(least_knit)
#print(most_knit)
#print(total_stitches)
#print(total_rows)