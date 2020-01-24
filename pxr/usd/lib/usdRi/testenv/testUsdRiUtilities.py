#!/pxrpythonsubst
#
# Copyright 2017 Pixar
#
# Licensed under the Apache License, Version 2.0 (the "Apache License")
# with the following modification; you may not use this file except in
# compliance with the Apache License and the following modification to it:
# Section 6. Trademarks. is deleted and replaced with:
#
# 6. Trademarks. This License does not grant permission to use the trade
#    names, trademarks, service marks, or product names of the Licensor
#    and its affiliates, except as required to comply with Section 4(c) of
#    the License and to reproduce the content of the NOTICE file.
#
# You may obtain a copy of the Apache License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the Apache License with the above modification is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the Apache License for the specific
# language governing permissions and limitations under the Apache License.
#

import unittest

from pxr.UsdRi import *

class TestUsdRiUtilities(unittest.TestCase):
  def test_RmanConversions(self):
      # Note that we have the old names as the first elements in
      # the list, our conversion test relies on this fact. This is only
      # really relevant in the case of Rman's '1' value, in which we have
      # some ambiguity(it could be cornersPlus1, cornersPlus2, or cornersOnly)
      # since we don't currently express the propogateCorners argument through
      # the system.
      faceVaryingConversionTable = [  
        (["all"], 0),
        (["cornersPlus1", "cornersPlus2", "cornersOnly"], 1),
        (["none"], 2),
        (["boundaries"], 3)]

      for tokens, rmanValue in faceVaryingConversionTable:
        # Check all tokens, old and new
        for token in tokens:
          # Convert to renderman values
          self.assertEqual(
            ConvertToRManFaceVaryingLinearInterpolation(token), rmanValue)

        # Convert from renderman values
        # Note that we only map to the new tokens.
        self.assertEqual(
          ConvertFromRManFaceVaryingLinearInterpolation(rmanValue), tokens[0])

if __name__ == "__main__":
  unittest.main()
