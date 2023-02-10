from argparse import ArgumentParser
from specs import SpecType

parser = ArgumentParser()

parser.add_argument('-s', '--spec-type', type=SpecType, choices=list(SpecType), help='choose from the specified set', required=True)
parser.add_argument('-i', '--input', type=str, help='SBOM file to be converted', required=True)
parser.add_argument('-o', '--output', type=str, help='path to output file. defaults to stdout.', required=False)

opts = parser.parse_args()


if opts.spec_type == SpecType.CYCLONEDX:
    from cyclonedx import CycloneDXTransformer
    transformer = CycloneDXTransformer(opts.input, opts.output)
    transformer.transform()
