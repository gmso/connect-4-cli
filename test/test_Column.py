import src.Column as Column
import src.Cell as Cell

def test_Column_construction():
    col = Column.Column()
    assert(col.rows_total == 6)
    assert(len(col.cells) == col.rows_total)
    assert(col.get_rows_empty() == col.rows_total)
    assert(col.get_rows_red() == 0)
    assert(col.get_rows_yellow() == 0)

def test_Column_add_checkers():
    col = Column.Column()
    assert(col.get_first_row_empty() == 0)
    assert(col.cells[0].is_empty() == True)

    col.add_checker_red()
    assert(col.get_first_row_empty() == 1)
    assert(col.cells[0].is_red() == True)

    col.add_checker_yellow()
    assert(col.get_first_row_empty() == 2)
    assert(col.cells[0].is_red() == True)
    assert(col.cells[1].is_yellow() == True)

    col.add_checker_red()
    assert(col.get_first_row_empty() == 3)
    assert(col.cells[0].is_red() == True)
    assert(col.cells[1].is_yellow() == True)
    assert(col.cells[2].is_red() == True)
