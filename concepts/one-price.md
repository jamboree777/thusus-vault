---
concept: one-price
type: concept
aliases: [Law of One Price, One Price, cross-exchange spread]
related: [executable-spread, mirage-arb, transfer-feasibility, quiet-size]
updated: 2026-07-16
author: thusus
source: nightwatch-kg
---

# One Price — the Law of One Price across exchanges

The Law of One Price says an identical asset should trade at the same price everywhere, because anyone can buy where it is cheap and sell where it is dear until the gap closes. Crypto is the natural laboratory for testing that law: the *same* token is listed on a dozen venues at once, and the price is never quite the same on any two of them.

NightWatch reads that gap across every exchange it scans. The interesting questions are not "is there a gap" — there is always a gap — but **where it breaks, how much, how often, and how fast it recovers.**

## Where and how much it breaks

Over a rolling 14-day window across roughly a million cross-exchange comparisons, venues sit on measurably different sides of the mid. Some venues habitually quote on the cheap side, some on the rich side (see [[coinbase]], [[binance]], and the per-venue notes for the observed leans). A gap is the distance between the cheapest ask and the richest bid at any moment.

## How often, and recovery

Most gaps are trivial and self-erasing: a bot lifts the cheap ask, hits the rich bid, and the two books converge within seconds. Those are not opportunities — by the time you see them they are gone. The gaps that *matter* are the ones that **persist**, and a gap persists only when something structural stops arbitrage from closing it:

- the token cannot actually move between the two venues ([[transfer-feasibility]]) — the classic [[mirage-arb]];
- one leg's book is a stranded ghost quote with no real depth behind it (see [[2026-03-24-btr-crash]]);
- a fiat border sits between the two venues ([[kimchi-premium]]).

So One Price is less a law than a diagnostic. When the gap won't close, the reason it won't close is usually the whole story. NightWatch's job is to tell you *which* reason applies, because that determines whether the gap is money or a [[mirage-arb|mirage]].

## Why the mid lies

A gap measured mid-to-mid is not a gap you can capture. What you can capture is the [[executable-spread]] — touch-to-touch, after fees, after [[quiet-size|footprint]], after the transfer. The distance between the two is where most "free money" evaporates.
