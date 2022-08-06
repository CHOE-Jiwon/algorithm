from datetime import datetime

time_pattern = "%Y-%m-%d %H:%M:%S"

def solution(n: int, logs: list):
    answer = []

    connections = {str(i):[] for i in range(n)}

    logs = [x.split(',') for x in logs]
    sorted_logs = sorted(logs, key = lambda x:(x[1], x[2], x[3]))

    transaction_record = {}

    for log in sorted_logs:
        sender_id, receiver_id, amount, created_at = log

        if receiver_id not in transaction_record:
            transaction_record[receiver_id] = dict()
        else:
            if amount not in transaction_record[receiver_id]:
                transaction_record[receiver_id][amount] = [[sender_id, created_at]]
            else:
                transaction_record[receiver_id][amount].append([sender_id, created_at])

    
    for user, tmp_record in transaction_record.items():

        for amount, sender_records in tmp_record.items():
            if len(sender_records) > 1:
                time_1 = datetime.strptime(sender_records[0][-1], time_pattern)
                time_2 = datetime.strptime(sender_records[-1][-1], time_pattern)

                diff_minute = (time_2 - time_1).seconds/60

                if diff_minute < 10:
                    connections[sender_records[0][0]].append(sender_records[1][0])
                    connections[sender_records[1][0]].append(sender_records[0][0])

    for k, v in connections.items():
        s, e = 0, 1

        for i in range(len(v)):
            for l in range(i+1, len(v)):
                if v[i] not in connections[v[l]] and v[l] not in connections[v[i]]:
                    connections[v[i]].append(v[l])
                    connections[v[l]].append(v[i])
    
    print([len(connections[x]) for x in connections])

    return answer



print(solution(6, ["5,0,72710000,2020-08-08 05:43:18","3,0,39222100,2020-11-04 02:19:50","4,5,89249000,2020-11-15 19:45:42","0,2,16230300,2020-12-13 01:45:17","2,5,89249000,2020-11-15 19:38:21","4,1,8453500,2020-08-30 20:40:39","0,1,92909400,2021-03-05 22:06:42","1,0,70403000,2020-12-07 21:41:39","0,5,96059000,2021-05-09 06:40:17","5,4,96161000,2020-10-04 07:57:43","3,2,71630300,2020-07-19 18:18:49","2,3,8796100,2020-08-12 21:28:13","4,2,81714500,2021-03-29 17:57:30","2,0,72710000,2020-08-08 05:34:15","4,3,18586200,2020-10-10 04:39:27","3,5,96059000,2021-05-09 06:47:36","0,2,48748300,2021-05-19 14:54:51","3,4,96161000,2020-10-04 07:57:21","2,1,71412600,2020-10-24 23:16:07","2,5,37973900,2021-06-27 11:40:01","0,5,37973900,2021-06-27 11:40:01","3,0,70403000,2020-12-07 21:46:55","5,1,54854500,2020-12-15 05:50:39"]))