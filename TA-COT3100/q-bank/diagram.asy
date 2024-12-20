unitsize(1cm);

path p = box((0,0),(1,1));

int dim = 2;

srand(round((cputime().parent.clock%1)*1e9));
int i_target = floor(unitrand()*dim);
int j_target = floor(unitrand()*dim);
draw((0.5,0.5));

for (int i=0; i<dim; ++i) {
  for (int j=0; j<dim; ++j) {
    if (i == i_target && j == j_target)
      filldraw(shift(i,j) * p, red, black);
    else
      filldraw(shift(i,j) * p, white, black);
  }
}
