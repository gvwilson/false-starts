# Documentation

## src/intro

## src/parse

### `src/parse/parse.py`: Parse messy data files.

-   class `State`: Enumerate possible parser states.
-   function `main`: Main driver.
-   function `is_empty`: Is this row effectively empty?
-   function `is_start_of_body`: Is this row the start of the body section?
-   function `load`: Load messy data.
-   function `normalize`: Remove leading spaces from rows if necessary.
-   function `parse_args`: Parse command-line arguments.
-   function `split`: Split header from body.

## src/center

### `src/center/display.py`: Analyze pollution readings.

-   function `main`: Main driver.
-   function `read_csv`: Read CSV files directly into dataframes.
-   function `read_db_pandas`: Read database tables into Pandas dataframes and manipulate.
-   function `read_db_sql`: Read tables and do calculations directly in SQL.
-   function `combine_with_pandas`: Combine tables using Pandas.
-   function `check`: Check all tables against each other.
-   function `make_figures`: Create figures showing calculated results.
-   function `parse_args`: Parse command-line arguments.

## src/script

### `src/script/invperc.py`: Invasion percolation in Python.

-   function `main`: Main driver.
-   function `make_grid`: Create a width X height grid.
-   function `choose_cell`: Choose the next cell to fill in.
-   function `adjacent`: Is (x, y) adjacent to a filled cell?
-   function `on_border`: Is this cell on the border of the grid?
-   function `print_grid`: Show the result.

## src/refactor

### `src/refactor/invperc.py`: Invasion percolation in Python.

-   function `main`: Main driver.
-   function `setup`: Get parameters.
-   function `initialize_grid`: Prepare grid for simulation.
-   function `fill_grid`: Fill grid one cell at a time.
-   function `choose_cell`: Choose the next cell to fill.
-   function `print_grid`: Show the result.

### `src/refactor/grid_list.py`: List-of-lists grid.

-   class `GridList`: Represent grid as list of lists.
    -   method `__init__`: Construct and fill.
    -   method `__getitem__`: Get value at location.
    -   method `__setitem__`: Set value at location.

### `src/refactor/grid_array.py`: NumPy array grid.

-   class `GridArray`: Represent grid as NumPy array.
    -   method `__init__`: Construct and fill.
    -   method `__getitem__`: Get value at location.
    -   method `__setitem__`: Set value at location.

### `src/refactor/grid_generic.py`: Represent 2D grid.

-   class `GridGeneric`: Represent a generic grid.
    -   method `__getitem__`: Get value at location.
    -   method `__setitem__`: Set value at location.
    -   method `__init__`: Record shared state.
    -   method `width`: Get width of grid.
    -   method `height`: Get height of grid.
    -   method `depth`: Get depth of grid.
    -   method `adjacent`: Is (x, y) adjacent to a filled cell?
    -   method `on_border`: Is this cell on the border of the grid?

## src/test

### `src/test/grid.py`: Represent 2D grid.

-   class `Grid`: Represent a grid.
    -   method `__init__`: Construct and fill.
    -   method `width`: Get width of grid.
    -   method `height`: Get height of grid.
    -   method `depth`: Get depth of grid.
    -   method `__getitem__`: Get value at location.
    -   method `__setitem__`: Set value at location.
    -   method `__eq__`: Compare to another grid.
    -   method `sweep`: Return indices and values in order.
    -   method `on_border`: Is this cell on the border of the grid?
    -   method `print`: Show the result.
    -   method `overwrite`: Overwrite with values.

### `src/test/invperc.py`: Invasion percolation in Python.

-   function `main`: Main driver.
-   function `setup`: Get parameters.
-   function `initialize_random`: Initialize RNG in reproducible way.
-   function `percolate`: Run all simulations.
-   function `calculate_density`: Calculate density versus distance from center of grid.

### `src/test/filler.py`: Manage filling.

-   class `Filler`: Manage grid filling.
    -   method `__init__`: Construct.
    -   method `grid`: Get the grid object.
    -   method `fill`: Fill grid one cell at a time.
    -   method `fill_first_cell`: Fill the initial cell.
    -   method `choose_cell`: Choose the next cell to fill.
    -   method `add_candidates`: Add candidates around (x, y).
    -   method `_add_candidate`: Add (x, y) if suitable.
    -   method `_randomize`: Randomize grid contents.

## src/perf

### `src/perf/invperc.py`: Invasion percolation in Python.

-   function `main`: Main driver.
-   function `setup`: Get parameters.
-   function `run_all`: Run all variations.
-   function `initialize_grid`: Prepare grid for simulation.
-   function `fill_grid`: Fill grid one cell at a time.
-   function `choose_cell`: Choose the next cell to fill.
-   function `check_equal`: Check that all grids got the same answer.
-   function `print_grid`: Show the result.

### `src/perf/grid_list.py`: List-of-lists grid.

-   class `GridList`: Represent grid as list of lists.
    -   method `__init__`: Construct and fill.
    -   method `__getitem__`: Get value at location.
    -   method `__setitem__`: Set value at location.

### `src/perf/grid_array.py`: NumPy array grid.

-   class `GridArray`: Represent grid as NumPy array.
    -   method `__init__`: Construct and fill.
    -   method `__getitem__`: Get value at location.
    -   method `__setitem__`: Set value at location.

### `src/perf/grid_generic.py`: Represent 2D grid.

-   class `GridGeneric`: Represent a generic grid.
    -   method `__getitem__`: Get value at location.
    -   method `__setitem__`: Set value at location.
    -   method `__init__`: Record shared state.
    -   method `width`: Get width of grid.
    -   method `height`: Get height of grid.
    -   method `depth`: Get depth of grid.
    -   method `__eq__`: Compare to another grid.
    -   method `adjacent`: Is (x, y) adjacent to a filled cell?
    -   method `on_border`: Is this cell on the border of the grid?

## src/flow

### `src/flow/analysis.py`: Analyze data from runs.

-   function `main`: Main driver.
-   function `parse_args`: Parse command-line arguments.

### `src/flow/invperc.py`: Invasion percolation in Python.

-   function `main`: Main driver.
-   function `parse_args`: Get parameters.
-   function `initialize_random`: Initialize RNG in reproducible way.
-   function `percolate`: Run all simulations.
-   function `initialize_grid`: Prepare grid for simulation.
-   function `fill_grid`: Fill grid one cell at a time.
-   function `choose_cell`: Choose the next cell to fill.
-   function `check_equal`: Check that all grids got the same answer.
-   function `print_grid`: Show the result.

### `src/flow/flow.py`: Re-run everything.

-   class `InvPercFlow`: Metaflow for invasion percolation.
    -   method `start`: Collect parameters and run jobs.
    -   method `run_job`: Run a sweep with one set of parameters.
    -   method `join`: Combine results from all sweeps.
    -   method `end`: Save results.

### `src/flow/grid_list.py`: List-of-lists grid.

-   class `GridList`: Represent grid as list of lists.
    -   method `__init__`: Construct and fill.
    -   method `__getitem__`: Get value at location.
    -   method `__setitem__`: Set value at location.

### `src/flow/grid_array.py`: NumPy array grid.

-   class `GridArray`: Represent grid as NumPy array.
    -   method `__init__`: Construct and fill.
    -   method `__getitem__`: Get value at location.
    -   method `__setitem__`: Set value at location.

### `src/flow/grid_generic.py`: Represent 2D grid.

-   class `GridGeneric`: Represent a generic grid.
    -   method `__getitem__`: Get value at location.
    -   method `__setitem__`: Set value at location.
    -   method `__init__`: Record shared state.
    -   method `width`: Get width of grid.
    -   method `height`: Get height of grid.
    -   method `depth`: Get depth of grid.
    -   method `__eq__`: Compare to another grid.
    -   method `adjacent`: Is (x, y) adjacent to a filled cell?
    -   method `on_border`: Is this cell on the border of the grid?

## src/lazy

### `src/lazy/analysis.py`: Analyze data from runs.

-   function `main`: Main driver.
-   function `parse_args`: Parse command-line arguments.

### `src/lazy/invperc.py`: Invasion percolation in Python.

-   function `main`: Main driver.
-   function `setup`: Get parameters.
-   function `initialize_random`: Initialize RNG in reproducible way.
-   function `percolate`: Run all simulations.
-   function `initialize_grid`: Prepare grid for simulation.
-   function `fill_grid`: Fill grid one cell at a time.
-   function `check_equal`: Check that all grids got the same answer.
-   function `print_grid`: Show the result.

### `src/lazy/flow.py`: Re-run everything.

-   class `InvPercFlow`: Metaflow for invasion percolation.
    -   method `start`: Collect parameters and run jobs.
    -   method `run_job`: Run a sweep with one set of parameters.
    -   method `join`: Combine results from all sweeps.
    -   method `end`: Save results.

### `src/lazy/grid_lazy.py`: Lazy-filling grid.

-   class `GridLazy`: Only look at cells that might actually be filled next time.
    -   method `__init__`: Construct and fill.
    -   method `fill_first_cell`: Fill the initial cell.
    -   method `choose_cell`: Choose the next cell to fill.
    -   method `add_candidates`: Add candidates around (x, y).
    -   method `_add_candidate`: Add (x, y) if suitable.

### `src/lazy/grid_list.py`: List-of-lists grid.

-   class `GridList`: Represent grid as list of lists.
    -   method `__init__`: Construct and fill.
    -   method `__getitem__`: Get value at location.
    -   method `__setitem__`: Set value at location.

### `src/lazy/grid_array.py`: NumPy array grid.

-   class `GridArray`: Represent grid as NumPy array.
    -   method `__init__`: Construct and fill.
    -   method `__getitem__`: Get value at location.
    -   method `__setitem__`: Set value at location.

### `src/lazy/grid_generic.py`: Represent 2D grid.

-   class `GridGeneric`: Represent a generic grid.
    -   method `__getitem__`: Get value at location.
    -   method `__setitem__`: Set value at location.
    -   method `__init__`: Record shared state.
    -   method `width`: Get width of grid.
    -   method `height`: Get height of grid.
    -   method `depth`: Get depth of grid.
    -   method `__eq__`: Compare to another grid.
    -   method `adjacent`: Is (x, y) adjacent to a filled cell?
    -   method `on_border`: Is this cell on the border of the grid?
    -   method `fill_first_cell`: Fill the initial cell.
    -   method `choose_cell`: Choose the next cell to fill.

## src/measure

### `src/measure/measure.py`: Measure fractal dimensions of grids.

-   function `main`: Main driver.
-   function `measure_density`: Calculate density versus distance from center of grid.
-   function `measure_dimension`: Measure fractal dimension of grid.
-   function `parse_args`: Parse command-line arguments.

### `src/measure/grid.py`: Represent 2D grid.

-   class `Grid`: Represent a grid.
    -   method `__init__`: Construct and fill.
    -   method `width`: Get width of grid.
    -   method `height`: Get height of grid.
    -   method `depth`: Get depth of grid.
    -   method `contents`: Get grid content.
    -   method `__getitem__`: Get value at location.
    -   method `__setitem__`: Set value at location.
    -   method `__eq__`: Compare to another grid.
    -   method `fill`: Fill grid one cell at a time.
    -   method `adjacent`: Is (x, y) adjacent to a filled cell?
    -   method `on_border`: Is this cell on the border of the grid?
    -   method `fill_first_cell`: Fill the initial cell.
    -   method `choose_cell`: Choose the next cell to fill.
    -   method `add_candidates`: Add candidates around (x, y).
    -   method `print`: Show the result.
    -   method `_add_candidate`: Add (x, y) if suitable.
    -   method `_init_grid`: Initialize grid contents.

### `src/measure/find_matching_files.py`: Check that generated files match saved files.


### `src/measure/invperc.py`: Invasion percolation in Python.

-   function `initialize_random`: Initialize RNG in reproducible way.
-   function `percolate`: Run all simulations.
-   function `main`: Main driver.
-   function `parse_args`: Get command-line parameters.

### `src/measure/flow.py`: Re-run everything.

-   class `InvPercFlow`: Metaflow for invasion percolation.
    -   method `start`: Collect parameters and run jobs.
    -   method `run_job`: Run a simulation with one set of parameters.
    -   method `join`: Join step required by Metaflow.
    -   method `end`: Wrap up.

## src/mut

### `src/mut/correlate.py`: Look for correlation between SNPs and snail size.

-   function `main`: Main driver.
-   function `parse_args`: Parse command-line arguments.
-   function `pivot_dataframe`: Turn (sequence, reading) into (loc, base, reading).
-   function `select_candidate_locs`: Select locations with more than one base.
-   function `plot`: Show standard plots of (subset of) data.

### `src/mut/make_snail_genomes.py`: Generate genomes with random mutations.

-   class `GenePool`: Keep track of generated genomes.
-   function `main`: Main driver.
-   function `add_susceptibility`: Add indication of genetic susceptibility.
-   function `parse_args`: Get command-line arguments.
-   function `random_bases`: Generate a random sequence of bases of the specified length.
-   function `random_genomes`: Generate a set of genomes with specified number of point mutations.
-   function `save`: Save or report generated.
-   function `_mutate_snps`: Introduce single nucleotide polymorphisms at the specified location.
-   function `_mutate_other`: Introduce up to `max_num_mutations` at specified locations.
-   function `_choose_one`: Convenience wrapper to choose a single items with weighted probabilities.
-   function `_other_bases`: Create a list of bases minus the one in the sequence at that location.

We return a list instead of a set because the result is used in random.choices(),
which requires an indexable sequence. We sort for reproducibility.

## src/query

### `src/query/query.py`: Query the plate database.

-   function `cli`: Command-line group.
-   function `count`: Count entries in database.
-   function `invalidated`: Display information about invalidated plates.
-   function `ls`: List entries in database.

### `src/query/query_pony.py`: Execute SQL queries using Pony ORM.

-   class `Staff`: Staff members.
-   class `Experiment`: Experiments.
-   class `Performed`: Who was involved in which experiments.
-   class `Plate`: Plates used in experiments.
-   class `Invalidated`: Invalidated plates.
-   function `query_pony`: Run query and show results.

### `src/query/query_direct.py`: Execute SQL queries directly.

-   function `query_direct`: Run query and show results.

### `src/query/make_raw_files.py`: Make plate files.

-   function `main`: Main driver.
-   function `parse_args`: Parse command-line arguments.

### `src/query/fill_tables.py`: Initialize database with previous experimental data.

-   function `main`: Main driver.
-   function `_fill_experiments`: Create experiments and their data.
-   function `_fill_staff`: Create people.
-   function `create_tables`: Create database tables.
-   function `invalidate_plates`: Invalidate a random set of plates.
-   function `parse_args`: Parse command-line arguments.
-   function `random_experiment_duration`: Choose random start date and end date for experiment.
-   function `random_filename`: Create a randomized filename.
-   function `random_plates`: Generate random plate data.
-   function `random_date_interval`: Choose a random end date (inclusive).
-   function `round_date`: Round time to whole day.
-   function `_date`: Format dates.

## src/service

### `src/service/server.py`: Basic data server.

-   function `index`: Display data server home page.
-   function `staff_index`: Display staff details.
-   function `experiment_index`: Display experiments.
-   function `plate_index`: Display available plates.
-   function `plate`: Display single plate.
-   function `_format_plate`: Read CSV and format as HTML.
-   function `_subpage`: Format links to plate pages.

### `src/service/model.py`: Execute SQL queries using Pony ORM.

-   class `Staff`: Staff members.
-   class `Experiment`: Experiments.
-   class `Performed`: Who was involved in which experiments.
-   class `Plate`: Plates used in experiments.
-   class `Invalidated`: Invalidated plates.
-   function `get_all`: Get all entries of particular kind.
-   function `get_count`: How many entries of the given kind?
-   function `get_plate_filename`: Where is the plate data stored?

## src/finale

## src/bib

## src/credits

