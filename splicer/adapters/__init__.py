from .. import Relation
from functools import partial 
class Adapter(object):
  """
  Adapter objects provide relations to the dataset.
  """

  @property
  def relations(self):
    """
    May return a list of name and schema of -some- of the relations 
    the adapter supports.
    
    Some adapters like HTTP etc.. will create tables on the fly
    based on the passed in URL so introspection is not possible
    """
    return []
    
  def get_relation(self, name):
    """Return the relation (table, view, etc..) with the given name or None if this
    adapter does not have the given table."""

  def has(self, relation):
    """Return true if the Adapter can resolve the relation"""

  def table_scan(self, name, ctx):
     raise NotImplementedError(
      '{} has not implemented table_scan'.format(
        self.__class__.__name__
      )
    )


  def evaluate(self,  loc):
    op = loc.node()
    #import pdb; pdb.set_trace()
    func = partial(self.table_scan, op.name)
    #func.schema = op.schema
    return loc.replace(Relation(self, op.name, self.schema(op.name), func))

  def schema(self, name):
    raise NotImplementedError(
      '{} has not implemented schema'.format(
        self.__class__.__name__
      )
    )
  