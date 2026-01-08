---
title: My own Calendar (with typst)
date: 2026-01-08
description: 
filetags: computers
---

I've been printing my own family calendar over the last year. However, most of the calendar templates I found online are ugly or boring. So obviously, I had to make my own:

<figure style="width: 100%; text-align: center;">
<img width="75%" src="/static/2026-01/Calendar.png" alt="The month of january, as rendered by my typst program" />
</figure>

Look, it has my local holidays and vacations!

The fun thing is, this was generated with [typst](https://typst.app/), which is a TeX-like markdown language that I wanted to play with for a while. But in contrast to TeX, it is easily programmable:

<aside class="code-box">

[calendar.typ](https://gist.github.com/bastibe/2881bb2eea02e18bfbc6ab3521cda8f3)
(Inspired by [a forum post](https://discuss.pixls.us/t/my-new-calendar-template-engine/53633))

```typst
#let YEAR = 2026

#let months = (
  "Januar", 
  "Februar", 
  "März", 
  "April", 
  "Mai", 
  "Juni", 
  "Juli", 
  "August", 
  "September", 
  "Oktober",
  "November", 
  "Dezember"
)
#let weekdays = (
  "Mo",
  "Di",
  "Mi",
  "Do",
  "Fr",
  "Sa",
  "So"
)
#let holidays = (
  "2026-01-01": "Neujahr",
  "2026-01-06": "Heilige Drei Könige",
  "2026-04-03": "Karfreitag",
  "2026-04-05": "Ostersonntag",
  "2026-04-06": "Ostermontag",
  "2026-05-01": "Tag der Arbeit",
  "2026-05-14": "Christi Himmelfahrt",
  "2026-05-24": "Pfingstsonntag",
  "2026-05-25": "Pfingstmontag",
  "2026-08-15": "Mariä Himmelfahrt",
  "2026-10-03": "Tag der Deutschen Einheit",
  "2026-11-01": "Allerheiligen",
  "2026-12-25": "1. Weihnachtstag",
  "2026-12-26": "2. Weihnachtstag"
)
#let vacations = (
  (from: "2025-12-22", to: "2026-01-05", name: "Weihnachtsferien"),
  (from: "2026-02-16", to: "2026-02-20", name: "Faschingsferien"),
  (from: "2026-03-30", to: "2026-04-10", name: "Osterferien"),
  (from: "2026-05-26", to: "2026-06-05", name: "Pfingstferien"),
  (from: "2026-08-03", to: "2026-09-14", name: "Sommerferien"),
  (from: "2026-11-02", to: "2026-11-06", name: "Herbstferien"),
  (from: "2026-12-24", to: "2027-01-08", name: "Weihnachtsferien")
)

#let str_to_date(s) = {
  let dateparts = s.split("-")
  datetime(
    year: int(dateparts.at(0)),
    month: int(dateparts.at(1)),
    day: int(dateparts.at(2)),
  )
}
#let is_vacation(dt) = {
  for vac in vacations {
    if dt >= str_to_date(vac.at("from")) and dt <= str_to_date(vac.at("to")) {
      return true
    }
  }
  return false
}

#let translated_month(dt) = months.at(dt.month() - 1)
#let translated_weekday(dt) = weekdays.at(dt.weekday() - 1)
#let day_color(dt) = if dt.weekday() in (6, 7) { rgb("#a91010") } else { black }
#let day_fill(dt) = if dt.display() in holidays.keys() { rgb("#e3e3e3") } else { white.transparentize(100%) }
#let day_stroke_h(dt) = if is_vacation(dt) { (top: 2pt + rgb("#a0a0a0")) } else { 0pt }
#let day_stroke_v(dt) = if is_vacation(dt) { (left: 2pt + rgb("#a0a0a0")) } else { 0pt }
#let max_date(a, b) = if a > b { a } else { b }
#let min_date(a, b) = if a < b { a } else { b }

#let calendar(year: "", body) = {

  set text(font: "Candara")
  set document(title: str(year) + " calendar")

  for month in range(1, 13) [

    #let month_date = datetime(
      year: year,
      month: month,
      day: 1,
    )

    #let monthly_days = ()
    #for day in range(0, 31) {
      let month_accumulator = (month_date + duration(days: day))
      if month_accumulator.month() != month {
        break
      }
      monthly_days.push(month_accumulator)
    }

    #let monthly_vacations = ()
    #for vac in vacations {
      let vac_start = str_to_date(vac.at("from"))
      let vac_end = str_to_date(vac.at("to"))
      if vac_end < monthly_days.at(0) or vac_start > monthly_days.at(-1) {
        continue
      }
      monthly_vacations.push(vac)
    }

    // ============= HORIZONTAL CALENDARIUM ==============

    #set page(height: 5cm, width: 21cm, margin: 10mm, fill: white.transparentize(50%))

    #let days_strip = table(
        columns: monthly_days.len(),
        rows: 2,
        align: center,
        inset: 0% + 4pt,
        stroke: 0pt,

        ..monthly_days.map(day => {
          table.cell(
            x: day.day() - 1,
            y: 1,
            fill: day_fill(day), 
            stroke: day_stroke_h(day),
          [
            #set text(size: 10pt, day_color(day))
            #translated_weekday(day)
          ])
        }),

        ..monthly_days.map(day => {
          table.cell(
            x: day.day() - 1,
            y: 2,
            fill: day_fill(day), [
            #set text(size: 12pt, day_color(day))
            #day.display("[day padding:none]")
          ])
        }),

        ..monthly_vacations.map(vac => {
          let vac_start_day = max_date(str_to_date(vac.at("from")), monthly_days.at(0))
          let vac_end_day = min_date(str_to_date(vac.at("to")), monthly_days.at(-1))
          let start_index = int((vac_start_day - monthly_days.at(0)).days())
          let span_days = int((vac_end_day - vac_start_day).days() + 1)

          table.cell(
            x: start_index,
            y: 0,
            colspan: span_days,
            align: center,
            [
              #set text(size: 10pt, rgb("#a0a0a0"))
              #vac.at("name")
            ]
          )
        })
    )

    #let month_header = text(size: 27pt, align(left, [#translated_month(month_date)]))

    #set par(spacing:0.5em)
    #month_header
    #days_strip

    #pagebreak(weak: true)

    // ===========================

    #set page(height: 21cm, width: 5cm, margin: 10mm, fill: white.transparentize(50%))

    #for lr in range(2) [
      #let curcol = if lr == 1 { (auto, 1fr) } else { (1fr, auto) }

      #let a = table(
          columns: 3,
          align: (left, left, right),
          inset: 0% + 4pt,
          stroke: 0pt,
          
          ..monthly_days.map(day => {
            table.cell(
              x: 1,
              y: day.day() - 1,
              fill: day_fill(day), 
              stroke: day_stroke_v(day),
              [
                #set text(size: 10pt, day_color(day))
                #translated_weekday(day)
              ])
          }),

          ..monthly_days.map(day => {
            table.cell(
              x: 2,
              y: day.day() - 1,
              fill: day_fill(day), [
              #set text(size: 12pt, day_color(day))
              #day.display("[day padding:space]")
            ])
          }),

          ..monthly_vacations.map(vac => {
            let vac_start_day = max_date(str_to_date(vac.at("from")), monthly_days.at(0))
            let vac_end_day = min_date(str_to_date(vac.at("to")), monthly_days.at(-1))
            let start_index = int((vac_start_day - monthly_days.at(0)).days())
            let span_days = int((vac_end_day - vac_start_day).days() + 1)

            table.cell(
              y: start_index,
              x: 0,
              rowspan: span_days,
              align: center + horizon,
              rotate(-90deg, reflow: false, origin: center + horizon,
                [
                  #set text(size: 10pt, rgb("#a0a0a0"))
                  #vac.at("name")
                ]
              )
            )
          }),
        )

      #let b = text(size: 27pt, align(right, rotate(-90deg, reflow: true, origin: top + right, [#translated_month(month_date)])))

      #grid(
        columns: curcol,
        align: (right, left),
        column-gutter: 10pt,
        if lr == 1 {b} else {a},
        if lr == 1 {a} else {b}
      )
      #pagebreak(weak: true)
    ]
  ]
}

#show: calendar.with(
  year: YEAR
)
```
</aside>

Typst was a complete joy to work with. It combines the notational ease of markdown with the layout chops of TeX and a simple, sane programming model.
