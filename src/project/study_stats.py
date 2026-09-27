import os
import csv

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"]=False

BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
png_path=os.path.join(BASE,"output","study_by_subject.png")
csv_path=os.path.join(BASE,"output","study_by_summary.csv")

all_days=["周一","周二","周三","周四","周五","周六","周日"]

class StudyRecord:
    def __init__(self,date,week,subject,minute,content):
        self.date=date
        self.week=week
        self.subject=subject
        self.minute=minute
        self.content=content
    def hours(self):
        return int(self.minute)/60
    def describe(self):
        return f"{self.date} {self.week} {self.subject} {self.hours()} {self.content}"

def load_records(path):
    #存入StudyRecord中
    try:
        BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        with open(os.path.join(BASE,path),"r",encoding="utf-8-sig") as f:
            rows=[]
            for row in csv.DictReader(f):
                rows.append(StudyRecord(row["日期"],row["周几"],row["科目"],row["分钟"],row["内容"]))
        return rows
    except FileNotFoundError:
        return []
records=load_records("data/study_log.csv")

def total_hours(records):
    # 总共几小时
    s=0
    for r in records:
        v=int(r.minute)/60
        s+=v
    return s
time=total_hours(records)

def by_subject(records):
    # 科目总时长
    d={}
    for r in records:
       d[r.subject]=d.get(r.subject,0)+int(r.minute)/60
    return d
data=by_subject(records)

def busiest_weekday(records):
    # 哪个周学习时长最多
    d={}
    for r in records:
        d[r.week]=d.get(r.week,0)+int(r.minute)/60
    return max(d.items(),key=lambda kv:kv[1])
max_week=busiest_weekday(records)

def missing_days(records, all_days):
    #哪个周没有学
    d={}
    for r in records:
        d[r.week]=d.get(r.week,0)+int(r.minute)/60
    result=[]
    for day in all_days:
        if d[day] == 0:
            result.append(day)
    return result
no_record=missing_days(records, all_days)

def plot_by_subject(data, outpath):
    # 画图
    item=sorted(data.items(),key=lambda kv:kv[1],reverse=True)
    labels=[kv[0] for kv in item]
    values=[kv[1] for kv in item]
    labels.reverse()
    values.reverse()
    fig,ax=plt.subplots(figsize=(8,4))
    ax.barh(labels,values,color="#F5A623")
    ax.set_title("各科目学习时长")
    ax.set_xlabel("小时数")
    for i,v in enumerate(values):
        ax.text(v + 0.1,i,str(v),va="center")
    fig.tight_layout()
    fig.savefig(outpath, dpi=100)
    plt.close(fig)
    return outpath

def save_summary(rows, csv_path):
    # 存入csv
    try:
        with open(csv_path,"w",encoding="utf-8-sig",newline="") as f:
            writer = csv.writer(f)
            for row in rows:
                writer.writerow(row)
        return len(rows)-1
    except FileNotFoundError:
        return []

def main():
    #主程序
    records=load_records("data/study_log.csv")
    t= total_hours(records)
    d = by_subject(records)
    plot_by_subject(d, png_path)
    mw = busiest_weekday(records)
    miss = missing_days(records, all_days)
    rows=[["指标","值"],
          ["记录条数",len(records)],
          ["总时长(小时)",round(t,2)],
          ["最忙的周几",mw[0]],
          ["最忙的周几时长(小时)",round(mw[1],2)],
          ["没学的周几","、".join(miss)]
          ]
    n = save_summary(rows,csv_path)
    print(f"共 {len(records)} 条记录，总时长 {t:.2f} 小时")
    print("最忙的周几：", mw[0])
    print("没学的周几：","、" .join(miss))
    print(f"已生成图 + CSV（{n} 行）")
if __name__ == '__main__':
    main()