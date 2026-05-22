# -*- coding: utf-8 -*-
import pytest

from gilded_rose import Item, GildedRose


def test_foo():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert "foo" == items[0].name


def test_normal_item_degrades_as_expected():
    """
    At the end of the day, the quality lowers by 1
    """
    items = [Item("foo", 5, 7)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 6


def test_normal_item_degrades_twice_as_fast_after_sell_by_date():
    """
    Once the sell by date has passed, `Quality` degrades twice as fast
    """
    items = [Item("bar", -1, 7)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 5


def test_normal_item_quality_is_never_negative():
    items = [Item("bar", 4, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0


def test_aged_brie_quality_increases():
    items = [Item("Aged Brie", 4, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 1


def test_aged_brie_quality_is_never_more_than_50():
    items = [Item("Aged Brie", 4, 50)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 50


@pytest.mark.parametrize("days", [11, 9, 4])
def test_backstage_passes_quality_is_never_more_than_50(days):
    items = [
        Item("Backstage passes to a TAFKAL80ETC concert", days, 50),
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 50


@pytest.mark.parametrize("days,expected_quality_increase", [(11, 1), (9, 2), (5, 3)])
def test_backstage_passes_quality_increase(days, expected_quality_increase):
    items = [Item("Backstage passes to a TAFKAL80ETC concert", days, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 20 + expected_quality_increase


def test_backstage_passes_after_the_concert():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0


def test_sulfuras_quality_never_changes():
    items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 80


@pytest.mark.xfail
def test_conjured_item_quality():
    items = [Item("Conjured foo", 11, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 18


def test_normal_sell_in_decreases_as_expected():
    """
    At the end of the day, the sell_in lowers by 1
    """
    items = [Item("foo", 5, 7)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 4


def test_sulfuras_sell_in_never_changes():
    items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 5


# TODO: Check error is raised if sell-in increases
