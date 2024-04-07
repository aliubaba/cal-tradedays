import datetime

def is_trading_day(date):
  """判断日期是否为交易日"""
  # 判断日期是否为周末
  if date.weekday() in [5, 6]:
    return False

  # 判断日期是否为节假日
  holidays = [
    datetime.date(2024, 4, 4),  # 清明节
    datetime.date(2024, 5, 1),  # 劳动节
    datetime.date(2024, 5, 2),  # 劳动节
    datetime.date(2024, 5, 3),  # 劳动节
    datetime.date(2024, 5, 4),  # 劳动节
    datetime.date(2024, 5, 5),  # 劳动节
    datetime.date(2024, 6, 10),  # 端午节
    datetime.date(2024, 9, 15),  # 中秋节
    datetime.date(2024, 9, 16),  # 中秋节
    datetime.date(2024, 9, 17),  # 中秋节
    datetime.date(2024, 10, 1),  # 国庆节
    datetime.date(2024, 10, 2),  # 国庆节
    datetime.date(2024, 10, 3),  # 国庆节
    datetime.date(2024, 10, 4),  # 国庆节
    datetime.date(2024, 10, 5),  # 国庆节
    datetime.date(2024, 10, 6),  # 国庆节
    datetime.date(2024, 10, 7),  # 国庆节
  ]

  if date in holidays:
    return False

  return True

def main():
  start_date = datetime.date(2024, 4, 8)
  end_date = datetime.date(2024, 12, 31)

  # 计算交易日数
  trading_day_count = 0
  for date in range((end_date - start_date).days + 1):
    date = start_date + datetime.timedelta(days=date)
    if is_trading_day(date):
      trading_day_count += 1

  print(f"从2024年4月8日至2025年1月1日，共有{trading_day_count}个交易日")

if __name__ == "__main__":
  main()
